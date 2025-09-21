from django.urls import path
from .views import AssignLessonView, StudentIncompleteLessonsView, MarkLessonCompleteView, TeacherAssignmentStatusView

urlpatterns = [
    path('assign/', AssignLessonView.as_view(), name='assign-lesson'),
    path('my-incomplete/', StudentIncompleteLessonsView.as_view(), name='my-incomplete-lessons'),
    path('complete/<int:pk>/', MarkLessonCompleteView.as_view(), name='mark-complete'),
    path('teacher-status/', TeacherAssignmentStatusView.as_view(), name='teacher-assignment-status'),
]
