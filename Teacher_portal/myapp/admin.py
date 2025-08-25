from django.contrib import admin
from .models import Student, SessionToken, Teacher, AuditLog
admin.site.register(Student)
admin.site.register(SessionToken)
admin.site.register(Teacher)
admin.site.register(AuditLog)

