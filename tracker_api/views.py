from django.shortcuts import render

from rest_framework import viewsets

from .serializers import AnswerSerializer
from .models import Answer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('date')
    serializer_class = AnswerSerializer
