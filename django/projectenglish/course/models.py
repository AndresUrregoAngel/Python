from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class PortalUsers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='course_users')
    profile = models.CharField(max_length=30)


class subject(models.Model):
    subj_name  = models.CharField(max_length=30)


class subject_category(models.Model):
    subject    = models.ForeignKey(subject, on_delete=models.CASCADE)
    category_name  = models.CharField(max_length=30)


class questions(models.Model):
    category  = models.ForeignKey(subject_category, on_delete=models.CASCADE)
    question_desc = models.CharField(max_length=1000)


class answer(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    category  = 	models.ForeignKey(subject_category, on_delete=models.CASCADE)
    questions = models.ForeignKey(questions, on_delete=models.CASCADE)
    answer_desc = models.CharField(max_length=500)
    correct = models.IntegerField()
