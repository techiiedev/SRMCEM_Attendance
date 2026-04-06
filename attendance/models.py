from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('TEACHER', 'Teacher'),
        ('CR', 'Class Representative'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='TEACHER')
    is_approved = models.BooleanField(default=False)

    # Resolve potential clashes with default auth groups/permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.'
    )

class Subject(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    def __str__(self): return f"{self.code} - {self.name}"

class Student(models.Model):
    university_roll = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    student_class = models.CharField(max_length=50)
    def __str__(self): return f"{self.university_roll} - {self.first_name}"

class AttendanceRecord(models.Model):
    student_class = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

class AttendanceStatus(models.Model):
    record = models.ForeignKey(AttendanceRecord, on_delete=models.CASCADE, related_name='statuses')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    class Meta:
        unique_together = ('record', 'student')