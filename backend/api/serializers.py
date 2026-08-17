"""Serializers for API."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Task serializer."""

    class Meta:
        """Meta class for Task serializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
