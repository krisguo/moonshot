from django.db import models
from django.contrib.auth.models import User



# id (primary key)
#
# title - string that will hold the title of the question
#
# description - string that will hold a string with the question itself
#
# author - will be connected by foreign key to django user model


class Question(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    author_id = models.ForeignKey('auth.User', related_name='questions', default='')


    class Meta:
        ordering = ['id', ]

