from student.serializers import *
from student.models import *
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

class Results(APIView):
    def get(self, request, pk):
        student = User.objects.get(pk=pk)
        studentExamList = StuExam_DB.objects.filter(student=student, completed=1)

        return Response({
            'student': UserSerializer(student).data,
            'paper': StuExam_DBSerializer(studentExamList, many=True).data
        })


    def post(self, request, pk):
        student = User.objects.get(pk=pk)
        paper = request.POST['paper']
        viewExam = StuExam_DB.objects.get(examname=paper, student=student)
        questions = viewExam.questions.all()

        return Response(
            {
                'exam': StuExam_DBSerializer(viewExam).data,
                'student': UserSerializer(student).data,
                'quesn': Stu_QuestionSerializer(questions, many=True).data
            }
        )
