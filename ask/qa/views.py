from django.shortcuts import render
from django.http import HttpResponse
from qa.models import *
from django.contrib.auth.models import User



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


def test_model(request, *args, **kwargs):
    user = User(username='x', password='y')
    user.save()
    question = Question(title='qwe', text='qwe', author=user)
    question.save()
    answer = Answer(text='qwe', question=question, author=user)
    answer.save()
    return HttpResponse(data, status=200)
