from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Lesson, Assignment
from .serializers import LessonSerializer, AssignmentSerializer
from django.contrib.auth.models import User
from django.utils import timezone

# View for assignments
class AssignmentViewSet(viewsets.ViewSet):
    
    # Teacher assigns a lesson
    def create(self, request):
        teacher_id = request.data.get('teacher')
        student_id = request.data.get('student')
        lesson_id = request.data.get('lesson')

        assignment = Assignment.objects.create(
            teacher_id=teacher_id,
            student_id=student_id,
            lesson_id=lesson_id
        )
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Student views incomplete lessons
    @action(detail=False, methods=['get'], url_path='my-lessons/(?P<student_id>[^/.]+)')
    def my_lessons(self, request, student_id=None):
        assignments = Assignment.objects.filter(student_id=student_id, completed=False)
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    # Student marks lesson as complete
    @action(detail=True, methods=['post'], url_path='complete')
    def complete_lesson(self, request, pk=None):
        assignment = Assignment.objects.get(id=pk)
        assignment.completed = True
        assignment.completed_at = timezone.now()
        assignment.save()
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)

    # Teacher checks completion
    @action(detail=False, methods=['get'], url_path='status/(?P<teacher_id>[^/.]+)')
    def status(self, request, teacher_id=None):
        assignments = Assignment.objects.filter(teacher_id=teacher_id)
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)
