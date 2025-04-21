from django.contrib import admin
from task_management.models import (
    Project,
    ProjectTask,
    Status,
    Task,
    TaskAssignment,
    TaskStatus,
    User,
)

# Register your models here.
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(ProjectTask)
admin.site.register(TaskAssignment)
admin.site.register(Status)
admin.site.register(TaskStatus)
