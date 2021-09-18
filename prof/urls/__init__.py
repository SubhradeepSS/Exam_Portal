from django.urls import path
from .. import views

# separate urls import
from .exam import urlpatterns as exam_urls
from .question import urlpatterns as question_urls
from .question_paper import urlpatterns as question_paper_urls
from .group import urlpatterns as group_urls
from .student import urlpatterns as student_urls

app_name = 'prof'

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += exam_urls
urlpatterns += question_paper_urls
urlpatterns += question_urls
urlpatterns += group_urls
urlpatterns += student_urls