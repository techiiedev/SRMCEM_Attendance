from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, Subject, AttendanceRecord, AttendanceStatus

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_approved', 'is_staff')
    list_filter = ('role', 'is_approved', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Approval Info', {'fields': ('role', 'is_approved')}),
    )

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(AttendanceRecord)
admin.site.register(AttendanceStatus)