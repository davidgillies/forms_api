from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import json


class Index(View):
    def get(self, request, a, b):
        out = {}
        out[a] = a
        out[b] = b
        # return HttpResponse('<title>%s %s</title>' % (a, b))
        return HttpResponse(json.dumps(out), content_type='application/json')
