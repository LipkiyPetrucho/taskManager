from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ("NEW", "Новая задача"),
        ("IN_PROGRESS", "В процессе работы"),
        ("SUCCESS", "Завершено успешно"),
        ("ERROR", "Ошибка"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="NEW")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
