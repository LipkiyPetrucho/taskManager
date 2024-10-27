# Task Manager API

## Описание
Task Manager — это API-сервис для управления задачами.
Сервис поддерживает создание задач через REST API и с использованием очереди сообщений (RabbitMQ).
Задачи имеют статусную модель и обрабатываются с эмуляцией выполнения и логированием результатов.

## Функциональные возможности
1. **Создание задач через REST API**
2. **Создание задач через очередь сообщений (RabbitMQ)**
3. **Статусная модель для задач**:
   - Новая задача
   - В процессе работы
   - Завершено успешно
   - Ошибка
4. **Эмуляция процесса обработки задач**
5. **Логирование процесса выполнения задач**
6. **Документация API через Swagger/OpenAPI**
7. **Контейнеризация через Docker**

***

## Стек технологий:
 - ![alt text](https://img.shields.io/badge/Python-3.12.4-grey?style=plastic&logo=python&logoColor=white&labelColor=%233776AB)

 - ![alt text](https://img.shields.io/badge/Django-5.1.2-grey?style=plastic&logo=django&logoColor=white&labelColor=%23092E20)

 - ![alt text](https://img.shields.io/badge/Docker-25.0.3-grey?style=plastic&logo=docker&logoColor=white&labelColor=2496ED)

 - ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.3-grey?style=plastic&logo=postgresql&logoColor=white&labelColor=336791)

 - ![alt text](https://img.shields.io/badge/RabbitMQ-3.13.7-grey?style=plastic&logo=rabbitmq&logoColor=white&labelColor=FF6600)

 - ![Swagger (drf-yasg)](https://img.shields.io/badge/Swagger%20(drf--yasg)-1.20.0-grey?style=plastic&logo=swagger&logoColor=white&labelColor=85EA2D)

***

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/LipkiyPetrucho/taskManager.git
cd task_manager
````

### 2. Настройка окружения
Создать файл .env на основе .env.sample и указать значения:

```dotenv
SECRET_KEY — секретный ключ Django
ALLOWED_HOSTS — список разрешённых хостов
POSTGRES_DB_NAME — имя базы данных PostgreSQL
POSTGRES_DB_USER — имя пользователя базы данных
POSTGRES_DB_PASSWORD — пароль пользователя базы данных
POSTGRES_DB_HOST — хост базы данных (например, db для контейнеризированной среды)
```

### 3. Сборка и запуск контейнеров

```bash
docker-compose up --build
```

При запуске будут созданы следующие контейнеры:

- web — Django-приложение
- worker — воркер для обработки задач
- db — база данных PostgreSQL
- rabbitmq — сервер очередей RabbitMQ
- nginx — прокси-сервер Nginx

### 4. Миграции и статические файлы
При первом запуске все миграции и сборка статических файлов будут выполнены автоматически.

***

## Документация API
Swagger-документация доступна по адресу http://localhost/swagger/.

## Примеры запросов
### 1. Создание новой задачи
**POST** `/api/tasks/`

Пример тела запроса:
```json
{
  "title": "Пример задачи",
  "description": "Описание задачи"
}
```
### 2. Получение информации о задаче
**GET** `/api/tasks/{id}/`

### 3. Получение списка задач с фильтрацией по статусу
**GET** `/api/tasks/?search=<STATUS>`

***

## Описание компонентов
### Producer (Отправка задач)
Модуль producer.py отправляет задачи в очередь RabbitMQ.
Он создает JSON-объект с информацией о задаче и публикует его в task_queue.

### Worker (Обработка задач)
Воркер, worker.py, подключается к RabbitMQ и обрабатывает задачи из task_queue. В ходе обработки он:
1. Устанавливает статус задачи в "В процессе работы".
2. Эмулирует выполнение задачи (случайная задержка 5-10 секунд).
3. Устанавливает случайный результат: "Завершено успешно" или "Ошибка".

### Логирование
Логирование всех операций доступно через консоль и позволяет отслеживать процесс обработки задач,
отправку и получение сообщений в очереди.

### Доступ администратора
Чтобы создать пользователя-администратора для доступа к панели администратора Django:
```bash
docker-compose exec web python manage.py createsuperuser
```
- ввести логин, например admin
- почту(опционально)
- ввести пароль, например admin

 зайти на http://127.0.0.1/admin/ либо http://localhost/admin/
- login: admin
- password: admin

### Для завершения работы необходимо:

 - Нажать комбинацию клавиш `CTRL + C` в окне терминала

### Запуск приложения
Как только контейнеры будут запущены, вы сможете получить доступ к приложению:
- Django Admin: http://localhost/admin
- API and Web Interface: http://localhost

### Тестирование
Для запуска тестов выполните команду:
```bash
docker-compose run web python manage.py test
```

***

## Примечания
 - В проекте использована библиотека drf-yasg для генерации Swagger-документации.
 - Воркер и веб-приложение находятся в отдельных контейнерах,
что позволяет удобно масштабировать их по мере необходимости.

***

## Авторы
 - Пётр Липатов - разработчик Task Manager API

***

### Лицензия
Проект распространяется по лицензии MIT.

***


<summary><b>Свяжитесь со мной:</b></summary>
   <p align="left">
       <a href="mailto:pafos.light@gmail.com"><img src="https://img.shields.io/badge/gmail-%23EA4335.svg?style=plastic&logo=gmail&logoColor=white" alt="Gmail"/></a>
       <a href="https://t.me/petr_lip"><img src="https://img.shields.io/badge/telegram-blue?style=plastic&logo=telegram&logoColor=white" alt="Telegram"/></a>
   </p>

