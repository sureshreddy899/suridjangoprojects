from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome_view(request):
    print('This line printed by view function while processing system')
    print(10/0)
    return HttpResponse('<h1>Custom Middleware Demo </h1>')
