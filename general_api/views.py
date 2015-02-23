from django.shortcuts import render
from django.http import HttpResponse


def index(request, a, b):
    return HttpResponse('<title>%s %s</title>' % (a, b))
