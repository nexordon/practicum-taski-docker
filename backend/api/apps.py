"""API applocation apps comfig."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Config for API application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
