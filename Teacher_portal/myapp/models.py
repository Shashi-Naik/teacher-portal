from django.db import models
import uuid

class Teacher(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=256)
    salt = models.CharField(max_length=32)

    def __str__(self):
        return self.username





class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.subject})"

class AuditLog(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    old_value = models.IntegerField()
    new_value = models.IntegerField()
    changed_at = models.DateTimeField(auto_now_add=True)


#========================================================================================
class SessionToken(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)






