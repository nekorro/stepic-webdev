from django.shortcuts import render
from django.http import HttpResponse


def http_resp_200(request, *args, **kwargs):
    return HttpResponse('OK', status=200)


def http_resp_404(request, *args, **kwargs):
    return HttpResponse('Not Found', status=404)
# Create your views here.
