from django.db import models
from main.models import *
from django.contrib.auth.models import User

# Create your models here.
class Stu_Question(Question_DB):
    professor = None
    student = models.ForeignKey(User, limit_choices_to={'groups__name': "Student"}, on_delete=models.CASCADE, null=True)
    choice = models.CharField(max_length=3, default="E")


class StuExam_DB(models.Model):
    student = models.ForeignKey(User, limit_choices_to={'groups__name': "Student"}, on_delete=models.CASCADE, null=True)
    examname = models.CharField(max_length=100)
    qpaper = models.ForeignKey(Question_Paper, on_delete=models.CASCADE, null=True)
    questions = models.ManyToManyField(Stu_Question)
    score = models.IntegerField(default=0)
    completed = models.IntegerField(default=0)


class StuResults_DB(models.Model):
    student = models.ForeignKey(User, limit_choices_to={'groups__name': "Student"}, on_delete=models.CASCADE, null=True)
    exams = models.ManyToManyField(StuExam_DB)
