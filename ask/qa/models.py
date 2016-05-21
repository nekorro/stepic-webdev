from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.


class QuestionManager(models.Manager):
    """docstring for QuestionManager"""
    def get_new(self):
        return self.order_by('-id')

    def get_popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User, related_name='question_author',
                               on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_by')
    objects = QuestionManager()

    def get_url(self):
        return reverse('question')

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title
