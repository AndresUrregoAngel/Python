from django.db import models

# Create your models here.

class subject(models.Model):
    subj_name  = models.CharField(max_length=30)


class questions(models.Model):
    question  = models.ForeignKey(subject, default= int, on_delete=models.CASCADE)
    question_desc = models.CharField(max_length=1000)


class answer(models.Model):
    option_sub =models.ForeignKey(subject,default= int, on_delete=models.CASCADE)
    option_que = models.ForeignKey(questions, default= int, on_delete=models.CASCADE)
    option_desc = models.CharField(max_length=500)
    correct = models.IntegerField()