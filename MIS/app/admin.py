from django.contrib import admin
from .models import Student,Internship,Education,Job,Job_groups,Intern_Info,Faculty,Staff,Semester_registered
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class StudentInline(admin.TabularInline):
    model = Student

class FacultyInline(admin.TabularInline):
    model = Faculty

class StaffInline(admin.TabularInline):
    model = Staff

class CustomUserAdmin(UserAdmin):
    inlines = [StudentInline, FacultyInline, StaffInline]

# Register your models here.
admin.site.register(Student)
admin.site.register(Education)
admin.site.register(Job_groups)
admin.site.register(Job)
admin.site.register(Intern_Info)
admin.site.register(Internship)
admin.site.register(Faculty)
admin.site.register(Staff)
admin.site.register(Semester_registered)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
