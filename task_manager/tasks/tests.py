from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task


class TaskTests(APITestCase):

    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'Test Task', 'description': 'This is a test task.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_get_task(self):
        task = Task.objects.create(title='Sample Task')
        url = reverse('task-detail', args=[task.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], task.title)

    def test_filter_tasks_by_status(self):
        Task.objects.create(title='Task 1', status='NEW')
        Task.objects.create(title='Task 2', status='SUCCESS')
        url = reverse('task-list') + '?search=SUCCESS'
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['status'], 'SUCCESS')
