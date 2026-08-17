"""Tests for API application."""

from http import HTTPStatus

from django.test import Client, TestCase

from . import models


class TaskiAPITestCase(TestCase):
    """Tests for Taski API."""

    def setUp(self) -> None:
        """Set up for tests."""
        self.guest_client = Client()

    def test_list_exists(self):
        """Check task list access."""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Check task create."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
