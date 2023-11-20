from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


def hello(request, number):
    return HttpResponse(f'Hello, World! {number}')

@csrf_exempt
def calc(request):
    data = json.loads(request.body)
    if(data['operation']=="+"):
        result = data['a'] + data['b']
    return HttpResponse(f"{result}")