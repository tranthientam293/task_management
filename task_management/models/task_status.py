from django.db import models

from accounts.models import User
from .task import Task
from .status import Status

class TaskStatus(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="statuses"
    )
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="tasks"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="task_status_updates"
    )
    updated_at = models.DateTimeField(auto_now=True)
    started_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-updated_at"]
