"""Admin panel for API."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Admin panel for Tasks."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
