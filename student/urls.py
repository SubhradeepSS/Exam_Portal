from django.urls import path, include
from . import views

app_name = 'student'

urlpatterns = [
                                # HOME
    path('', views.index, name='index'),
    
                                # EXAM
    path('exams', views.exams, name='exams'),
    path('results', views.results, name='results'),

    path('api/', include('student.api.urls')),
]
