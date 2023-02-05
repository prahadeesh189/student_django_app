from rest_framework import serializers
from stu_app.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['Id','name','branch','college_name']


