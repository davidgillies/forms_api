from django.shortcuts import render
from django.http import HttpResponse


def index(request, a):
    return HttpResponse('<title>%s</title>' % a)
