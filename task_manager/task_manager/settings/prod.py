import os

from .base import *

DEBUG = False

ADMINS = [
    ("Petr L", "bang1987@mail.ru"),
]

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("POSTGRES_DB_HOST"),
        "NAME": os.getenv("POSTGRES_DB_NAME"),
        "USER": os.getenv("POSTGRES_DB_USER"),
        "PASSWORD": os.getenv("POSTGRES_DB_PASSWORD"),
        "PORT": 5432,
    }
}

# POSTGRES_DB: task_db
# POSTGRES_USER: task_db_user
# POSTGRES_PASSWORD: task_db_password
