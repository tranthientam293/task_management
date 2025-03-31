from django.contrib import admin
from .models import Role, User, Task, Project, ProjectTask, TaskAssignment, Status, TaskStatus

# Register your models here.
admin.site.resgiter(Role)
admin.site.resgiter(User)
admin.site.resgiter(Task)
admin.site.resgiter(Project)
admin.site.resgiter(ProjectTask)
admin.site.resgiter(TaskAssignment)
admin.site.resgiter(Status)
admin.site.resgiter(TaskStatus)
