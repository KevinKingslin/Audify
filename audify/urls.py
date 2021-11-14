from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("index", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]