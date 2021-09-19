from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from student.models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class StuExam_DBSerializer(ModelSerializer):
    class Meta:
        model = StuExam_DB
        fields = '__all__'


class Stu_QuestionSerializer(ModelSerializer):
    class Meta:
        model = Stu_Question
        fields = '__all__'
        