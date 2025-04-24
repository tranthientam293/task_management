from django.contrib.auth import login, logout
from django.contrib.auth.views import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from accounts.forms import LoginForm, RegisterForm


def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            login(request, form.user)
            return redirect(reverse("index"))

    return render(
        request,
        "accounts/login.html",
        {
            "form": form,
        },
    )

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse("login"))


def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse("login"))
    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        },
    )

