from django.urls import path
from . import views

urlpatterns = [
    path('question', views.add_question, name='add_question'),
    path('question/view_all_ques', views.view_all_ques, name='view_all_ques'),
]