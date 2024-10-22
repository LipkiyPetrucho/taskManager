import json
import pika
import logging

logger = logging.getLogger(__name__)

def send_task(task_data):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()

        channel.queue_declare(queue='task_queue', durable=True)
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=json.dumps(task_data),
            properties=pika.BasicProperties(
                delivery_mode=2,
            ))
        logger.info(" [x] Sent %r", task_data)
    except pika.exceptions.AMQPError as e:
        logger.error("Failed to send task to RabbitMQ: %s", e)
    finally:
        if 'connection' in locals() and connection.is_open:
            connection.close()
