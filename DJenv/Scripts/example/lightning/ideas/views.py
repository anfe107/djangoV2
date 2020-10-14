from django.shortcuts import render
from django.http import HttpResponse

# TODO  defined index function (view) for simple output

def index(request):
    return HttpResponse('Ideenspeicher')
