from django.contrib import admin
from .models import Student,Internship,Education,Job,Job_groups,Intern_Info,Faculty,Staff,Semester_registered

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
