from django.db import models
from students.models import Student
from courses.models import Course


class Grade(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    marks = models.IntegerField()

    grade = models.CharField(
        max_length=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
    

    def save(self, *args, **kwargs):

        if self.marks >= 90:
            self.grade = 'A+'

        elif self.marks >= 80:
            self.grade = 'A'

        elif self.marks >= 70:
            self.grade = 'B'

        elif self.marks >= 60:
            self.grade = 'C'

        else:
            self.grade = 'F'

        super().save(*args, **kwargs)