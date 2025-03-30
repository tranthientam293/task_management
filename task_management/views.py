from django.shortcuts import render

def index(request):
    return render(request, 'task_management/index.html')
