from django.urls import path
from .views import AssignLessonView, StudentIncompleteLessonsView, MarkLessonCompleteView, TeacherAssignmentStatusView

urlpatterns = [
    path('assignments/assign/', AssignLessonView.as_view(), name='assign-lesson'),
    path('assignments/my-incomplete/', StudentIncompleteLessonsView.as_view(), name='my-incomplete-lessons'),
    path('assignments/complete/<int:pk>/', MarkLessonCompleteView.as_view(), name='mark-complete'),
    path('assignments/teacher-status/', TeacherAssignmentStatusView.as_view(), name='teacher-assignment-status'),
]

    