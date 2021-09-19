from rest_framework.serializers import ModelSerializer

from main.models import Question_Paper


class Question_PaperSerializer(ModelSerializer):
    class Meta:
        model = Question_Paper
        fields = '__all__'
