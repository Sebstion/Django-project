from django.shortcuts import render
from django.http import HttpResponse

def hello(request, number):
    return HttpResponse(f'Hello, World! {number}')

def calc(request):
    pass