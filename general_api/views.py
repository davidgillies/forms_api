from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import json


class Index(View):
    def get(self, request, xml=None, section=None, id_variable=None,
            id_variable_value=None):
        out = {}
        out['xml'] = xml
        out['section'] = section
        out['id_variable'] = id_variable
        out['id_variable_value'] = id_variable_value
        out['get_var'] = request.GET
        return HttpResponse(json.dumps(out), content_type='application/json')
