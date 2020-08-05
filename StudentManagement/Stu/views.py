#from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentInfoSerializer
from .models import StudentInfo


class StudentInfoViewSet(ModelViewSet):
    serializer_class = StudentInfoSerializer
    queryset = StudentInfo.objects.all()