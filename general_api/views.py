from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class Index(View):
    def get(self, request, a, b):
        return HttpResponse('<title>%s %s</title>' % (a, b))
