from django.urls import path
from . import views

urlpatterns = [
    path('exams', views.view_exams, name='view_exams'),
    path('exams/<int:exam_id>', views.view_exam, name='view_exam'),
    path('exams/<int:exam_id>/edit', views.edit_exam, name='edit_exam'),
    path('exams/<int:exam_id>/delete', views.delete_exam, name='delete_exam'),
]