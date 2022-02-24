import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

class JSendFormatter(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if hasattr(response, 'data'):
            # NOTE Other status codes needs to be included in here.
            if response.status_code == 200:
                response.data = {
                    "status": "success",
                    "data": response.data
                }
            else:
                response.data = {
                    "status": "failed",
                    "data": response.data
                }
        return response
