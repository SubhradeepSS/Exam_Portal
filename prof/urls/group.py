from django.urls import path
from . import views

urlpatterns = [
    path('viewgroups', views.create_student_group, name='view_groups'),
    path('viewgroups/<int:group_id>', views.view_specific_group, name='view_specific_group'),
    path('viewgroups/<int:group_id>/students', views.view_student_in_group, name='view_students_in_group'),
    path('viewgroups/<int:group_id>/edit', views.edit_group, name='edit_group'),
    path('viewgroups/<int:group_id>/edit/delete', views.delete_group, name='delete_group'),
]