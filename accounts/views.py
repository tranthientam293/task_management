from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import login_required, LoginView
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from accounts.forms import LoginForm, RegisterForm


class RegisterView(View):
    form_class = RegisterForm
    initial = {"key": "value"}
    template_name = "accounts/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "User created successfully")
            return redirect(reverse("login"))

        return render(request, self.template_name, {"form": form})


class AccountLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse("login"))
