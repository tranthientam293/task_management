from django.db import models

from .task import Task
from .user import User


class TaskAssignment(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="assignments",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assigned_users"
    )

    class Meta:
        unique_together = ("task", "user")
