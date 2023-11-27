from django.urls import path
from .views import hello, calc, get_users, add_user, login

urlpatterns = [
    path('hello/<int:number>', hello),
    path('calc', calc),
    path('users', get_users),
    path('add_user', add_user),
    path('login', login),
]