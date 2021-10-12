from django.db.models import fields
from rest_framework import serializers
from .models import Student



class StudentSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city','pass_by']
        