from django.contrib import admin
from .models import Role, User, Task, Project, ProjectTask, TaskAssignment, Status, TaskStatus

# Register your models here.
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(ProjectTask)
admin.site.register(TaskAssignment)
admin.site.register(Status)
admin.site.register(TaskStatus)
