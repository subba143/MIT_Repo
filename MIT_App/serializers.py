from rest_framework import serializers
from .models import Institute, Course, Student, Profile

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='name.student_name')
    institute_name = serializers.CharField(source='name.institute.institute_name')
    course_name = serializers.CharField(source='name.course.course_name')

    class Meta:
        model = Profile
        fields = ['student_name', 'institute_name', 'course_name', 'photo', 'resume']
