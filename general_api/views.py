from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View
import json
import apps_xml


class Index(View):
    def get(self, request, xml=None, section=None, id_variable=None,
            id_variable_value=None):
        if id_variable is None or id_variable_value is None:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        else:
            data = apps_xml.apps[xml].get_data(section, id_variable, id_variable_value)
#        app = apps_xml.apps[xml]
#        section = app.get_section(section)
#        out = {}
#        out['xml'] = xml
#        out['section'] = section.attrib['position']
#        out['id_variable'] = id_variable
#        out['id_variable_value'] = id_variable_value
#        out['get_var'] = request.GET
#        out['filename'] = apps_xml.apps[xml].name
            return HttpResponse(json.dumps(data), content_type='application/json')

    def post(self, request, xml=None, section=None, id_variable=None,
             id_variable_value=None):
        data = apps_xml.apps[xml].insert_data(section, id_variable, id_variable_value, request.body)
        return HttpResponse(json.dumps(data), content_type='application/json', status=201)

    def put(self, request, xml=None, section=None, id_variable=None,
             id_variable_value=None):
        data = apps_xml.apps[xml].update_data(section, id_variable, id_variable_value, request.body)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def delete(self, request, xml=None, section=None, id_variable=None,
             id_variable_value=None):
        data = apps_xml.apps[xml].delete_data(section, id_variable, id_variable_value)
        return HttpResponse(None, status=204)
