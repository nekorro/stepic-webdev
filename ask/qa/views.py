from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from qa.models import Question, Answer
from ask.custom_paginate import paginate


def http_resp_200(request, *args, **kwargs):
    if args:
        data = args[0]
    else:
        data = 'OK'
    return HttpResponse(data, status=200)


def http_resp_404(request, *args, **kwargs):
    return HttpResponse('Not Found', status=404)


def test_template(request, *args, **kwargs):
    return render(request, 'test_index.html')


def test_model(request, *args, **kwargs):
    user = User(username='o', password='o')
    user.save()
    question = Question(title='qwe', text='qwe', author=user)
    question.save()
    answer = Answer(text='qwe', question=question, author=user)
    answer.save()
    return HttpResponse('OK', status=200)


@require_GET
def home_page(request, *args, **kwargs):
    questions = Question.objects.get_new()
    paginator, page = paginate(request, questions)
    paginator.baseurl = reverse('home')
    return render(request, 'qa/question_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        })


@require_GET
def popular_questions_page(request, *args, **kwargs):
    questions = Question.objects.get_popular()
    paginator, page = paginate(request, questions)
    paginator.baseurl = reverse('popular')
    return render(request, 'qa/question_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        })


@require_GET
def question_details_page(request, *args, **kwargs):
    question = get_object_or_404(Question, id=kwargs['id'])
    return render(request, 'qa/question_details.html', {
        'question': question,
        'answers': question.answer_set.all()[:],
        })
