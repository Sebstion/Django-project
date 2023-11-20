from django.urls import path
from .views import hello, calc

urlpatterns = [
    path('hello/<int:number>', hello),
    path('calc', calc),
]