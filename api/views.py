from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.models import Student
from api.serializer import StudentSerilalizer

# Create your views here.

class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerilalizer
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(pass_by = user)
    
