from student.serializers import *
from student.models import *
from main.serializers import Question_PaperSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils import timezone
from django.contrib.auth.models import User


class Exam(APIView):
    def get(self, request, pk):
        student = User.objects.get(pk=pk)
        studentExamsList = StuExam_DB.objects.filter(student=student)

        return Response({
            'student': UserSerializer(student).data, 
            'paper': StuExam_DBSerializer(studentExamsList, many=True).data
        })

    
    def post(self, request, pk):
        student = User.objects.get(pk=pk)

        if not request.POST.get('papertitle', False):
            paper = request.POST['paper']
            stuExam = StuExam_DB.objects.get(examname=paper, student=student)
            qPaper = stuExam.qpaper
            examMain = Exam_Model.objects.get(name=paper)

            # TIME COMPARISON
            exam_start_time = examMain.start_time
            curr_time = timezone.now()

            if curr_time < exam_start_time:
                return Response({'time': 'Time expired'})


            stuExam.questions.all().delete()

            qPaperQuestionsList = qPaper.questions.all()
            for ques in qPaperQuestionsList:
                student_question = Stu_Question(question=ques.question, optionA=ques.optionA, optionB=ques.optionB,
                                                optionC=ques.optionC, optionD=ques.optionD,
                                                answer=ques.answer, student=student)
                student_question.save()
                stuExam.questions.add(student_question)
                stuExam.save()

            stuExam.completed = 1
            stuExam.save()
            mins = examMain.duration
            secs = 0

            return Response({
                'qpaper': Question_PaperSerializer(qPaper).data, 
                'question_list': Stu_QuestionSerializer(stuExam.questions.all(), many=True).data, 
                'student': UserSerializer(student).data, 
                'exam': paper, 
                'min': mins, 'sec': secs
            })


        else:
            paper = request.POST['paper']
            title = request.POST['papertitle']
            stuExam = StuExam_DB.objects.get(examname=paper, student=student)
            qPaper = stuExam.qpaper

            examQuestionsList = stuExam.questions.all()
            examScore = 0
            for ques in examQuestionsList:
                ans = request.POST.get(ques.question, False)
                if not ans:
                    ans = "E"
                ques.choice = ans
                ques.save()
                if ans == ques.answer:
                    examScore = examScore + 1

            stuExam.score = examScore
            stuExam.save()

            return Response({
                'Title': title, 
                'Score': examScore, 
                'student': UserSerializer(student).data
            })