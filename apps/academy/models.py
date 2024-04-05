from django.db import models


class Student(models.Model):
    """A model to manage students info"""

    identifier = models.IntegerField("Identifier")
    name = models.CharField("Name", max_length=100)
    phone = models.IntegerField("Phone")

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name


class Assignment(models.Model):
    """A model to manage assignments"""

    name = models.CharField("Name", max_length=50)

    class Meta:
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"

    def __str__(self):
        return self.name


class StudentAssignment(models.Model):
    """A model to manage the students assignments"""

    student = models.ForeignKey(
        Student, verbose_name="Student", on_delete=models.CASCADE
    )
    assignment = models.ForeignKey(
        Assignment, verbose_name="Assignment", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Student Assignments"
        verbose_name_plural = "Students Assignments"

    def __str__(self):
        return f"{self.student.name} - {self.assignment.name}"
