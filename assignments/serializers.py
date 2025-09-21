from rest_framework import serializers
from .models import Assignment

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'teacher', 'student', 'lesson', 'completed', 'assigned_at', 'completed_at']
        read_only_fields = ['id', 'assigned_at', 'completed_at']
