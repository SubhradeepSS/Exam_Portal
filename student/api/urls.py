from student.views.exams import exams
from django.urls import path, include
from . import results, exams

urlpatterns = [
    path('results/<int:pk>', results.Results.as_view()),
    path('exams/<int:pk>', exams.Exam.as_view()),
]
