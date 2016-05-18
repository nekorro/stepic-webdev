from django.shortcuts import render
from django.http import HttpResponse


def http_resp_200(request, *args, **kwargs):
    if args:
        data = args[0]
    else:
        data = 'OK'
    return HttpResponse(data, status=200)


def http_resp_404(request, *args, **kwargs):
    return HttpResponse('Not Found', status=404)
# Create your views here.


def test_template(request, *args, **kwargs):
    return render(request, 'test_index.html')
