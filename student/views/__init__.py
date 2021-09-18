from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from main.models import *
from django.contrib.auth.models import User
from student.models import *

from .exams import *
from .result import *

# Create your views here.


def index(request):
    student = request.user

    studentGroup = Special_Students.objects.filter(students=student)
    examsList = []
    if studentGroup.exists():
        for student_ in studentGroup:
            stud_exams = Exam_Model.objects.filter(student_group=student_)
            if stud_exams.exists():
                if stud_exams.count() > 1:
                    for stud_exam in stud_exams:
                        examsList.append(stud_exam)
                else:
                    examsList.append(Exam_Model.objects.get(
                        student_group=student_))

    if examsList:
        for exam in examsList:
            currentExamList = StuExam_DB.objects.filter(
                examname=exam.name, student=student)

            if not currentExamList.exists():  # If no exam are there in then add exams
                tempExam = StuExam_DB(student=student, examname=exam.name,
                                        qpaper=exam.question_paper, score=0, completed=0)
                tempExam.save()
                exam_question_paper = exam.question_paper
                questions_in_paper = exam_question_paper.questions.all()
                
                for ques in questions_in_paper:
                    # add all the questions from the prof to student database
                    studentQuestion = Stu_Question(question=ques.question, optionA=ques.optionA, optionB=ques.optionB,
                                                    optionC=ques.optionC, optionD=ques.optionD,
                                                    answer=ques.answer, student=student)
                    studentQuestion.save()
                    tempExam.questions.add(studentQuestion)

    return render(request, 'student/index.html', {
        'stud': student
    })
