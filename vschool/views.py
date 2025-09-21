from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

from vschool.models import Lesson
from assignments.models import Assignment
from .serializers import AssignmentSerializer

# ------------------------------
# Assign a lesson (teacher assigns to student)
# ------------------------------
class AssignLessonView(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

# ------------------------------
# List incomplete lessons for a student
# ------------------------------
class StudentIncompleteLessonsView(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Assignment.objects.filter(student=self.request.user, completed=False)

# ------------------------------
# Mark a lesson as complete (student)
# ------------------------------
class MarkLessonCompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # fixed

    def post(self, request, pk):
        try:
            assignment = Assignment.objects.get(pk=pk, student=request.user)
        except Assignment.DoesNotExist:
            return Response(
                {"detail": "No Assignment matches the given query."},
                status=status.HTTP_404_NOT_FOUND
            )

        assignment.completed = True
        assignment.completed_at = timezone.now()
        assignment.save()

        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)

# ------------------------------
# View teacher's assignments and their status
# ------------------------------
class TeacherAssignmentStatusView(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Assignment.objects.filter(teacher=self.request.user)
