from django.contrib.auth.views import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, "task_management/index.html")
