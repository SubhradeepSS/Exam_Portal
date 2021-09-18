from django.urls import path
from . import views

urlpatterns = [
    path('students', views.view_students, name='view_students'),
]