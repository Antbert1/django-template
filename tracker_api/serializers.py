from rest_framework import serializers

from .models import Answer

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('question', 'date', 'value', 'period')
