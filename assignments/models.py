from django.db import models
from django.contrib.auth.models import User
from vschool.models import Lesson  # import Lesson from vschool app

class Assignment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_lessons_assignments')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_to_me_assignments')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_assignments')
    completed = models.BooleanField(default=False)
    assigned_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.lesson.title} -> {self.student.username}"
