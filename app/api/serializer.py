from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from vvmstk.models import Groups_students, Students

class Group_studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups_students
        fields = ['id',
                  'group_name', 
                  'group_date_begin',
                  'group_date_end', 
                  'kategory', 
                  'price', 
                  'time_study']


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'