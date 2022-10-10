import datetime

from django.db import models
from django.utils import timezone

"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
"""


class Post(models.Model):
    post_title = models.CharField(max_length=42)
    post_text = models.TextField()
    post_date = models.DateTimeField('date_published')
    post_image = models.ImageField(upload_to="media")
    post_hidden = models.BooleanField(default = False)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=16)
    comment_text = models.CharField(max_length=250)
    comment_date = models.DateTimeField('date_published', default = None)

    def __str__(self):
        return self.comment_text