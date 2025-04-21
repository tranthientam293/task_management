from django.db import models

from .task import Task
from .project import Project


class ProjectTask(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    class Meta:
        unique_together = ("project", "task")
