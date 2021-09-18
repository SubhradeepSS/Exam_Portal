from django.urls import path
from . import views

urlpatterns = [
    path('questionpaper', views.make_paper ,name='make_paper') ,
    path('questionpaper/addquestion',views.add_question_in_paper, name="add_question_in_paper"),
    path('questionpaper/viewpaper',views.view_paper,name='view_paper'),
    path('questionpaper/editpaper',views.edit_paper,name='edit_paper'),
    path('questionpaper/viewpaper/<int:paper_id>', views.view_specific_paper, name='view_specific_paper'),
    path('question/view_all_ques/edit_question/<int:ques_qno>',views.edit_question,name="edit_question"),
]