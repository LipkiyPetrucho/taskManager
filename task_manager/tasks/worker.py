# Настройка Django окружения
import json
import logging
import os
import random
import sys
import time

import django
import pika

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
django.setup()

from tasks.models import Task

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_task(ch, method, properties, body):
    task_data = json.loads(body)
    try:
        task = Task.objects.get(id=task_data['id'])
        task.status = 'IN_PROGRESS'
        task.save()
        logger.info(f"Task {task.id} is in progress.")

        delay = random.randint(5, 10)
        time.sleep(delay)

        if random.choice([True, False]):
            task.status = 'SUCCESS'
            logger.info(f"Task {task.id} completed successfully.")
        else:
            task.status = 'ERROR'
            logger.error(f"Task {task.id} failed.")
        task.save()
    except Task.DoesNotExist:
        logger.error(f"Task with id {task_data['id']} does not exist.")

    finally:
        ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
            break
        except pika.exceptions.AMQPConnectionError as e:
            logger.error("Failed to connect to RabbitMQ, retrying in 5 seconds...")
            time.sleep(5)

    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=process_task)

    logger.info(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()