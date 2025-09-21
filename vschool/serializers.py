from rest_framework import serializers
from vschool.models import Lesson
from assignments.models import Assignment

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description']

class AssignmentSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = Assignment
        fields = ['id', 'teacher', 'student', 'lesson', 'completed', 'assigned_at', 'completed_at']
