from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Assignment
from .serializers import AssignmentSerializer
from django.utils import timezone

# 1️⃣ Teacher assigns a lesson
class AssignLessonView(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users

# 2️⃣ Student views incomplete lessons
class StudentIncompleteLessonsView(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Assignment.objects.filter(student=self.request.user, completed=False)

# 3️⃣ Student marks lesson as complete
class MarkLessonCompleteView(generics.UpdateAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Assignment.objects.all()

    def perform_update(self, serializer):
        serializer.save(completed=True, completed_at=timezone.now())

# 4️⃣ Teacher views completion status (optional)
class TeacherAssignmentStatusView(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Assignment.objects.filter(teacher=self.request.user)

