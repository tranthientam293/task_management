from django.urls import path

from .views import AccountLoginView, RegisterView, logout_view

urlpatterns = [
    path("login", AccountLoginView.as_view(), name="login"),
    path("logout", logout_view, name="logout"),
    path("register", RegisterView.as_view(), name="register"),
]
