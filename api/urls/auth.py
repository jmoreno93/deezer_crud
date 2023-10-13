from api.views import login, logout, register_user
from django.urls import path

urlpatterns = [
    path("login/", login),
    path("logout/", logout),
    path("register/", register_user),
]
