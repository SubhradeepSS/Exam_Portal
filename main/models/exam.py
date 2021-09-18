from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from datetime import datetime
from .group import Special_Students
from .question_paper import Question_Paper

class Exam_Model(models.Model):
    professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    total_marks = models.IntegerField()
    duration = models.IntegerField()
    question_paper = models.ForeignKey(Question_Paper, on_delete=models.CASCADE, related_name='exams')
    student_group = models.ManyToManyField(Special_Students, related_name='exams')
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name


class ExamForm(ModelForm):
    class Meta:
        model = Exam_Model
        fields = '__all__'
        exclude = ['professor']