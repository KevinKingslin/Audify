from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="login"),
    path("login", views.login_view, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]