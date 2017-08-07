from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        return redirect('app/welcome.html')
    else:
        return render(request,'app/index.html')


def welcome(request):
    return render(request,'app/welcome.html')


def contact(request):
    return render(request,'app/contact.html')


def education(request):
    return render(request, 'app/education.html')


def internship_type(request):
    return render(request, 'app/internship-type.html')


def internship_info(request):
    return render(request,'app/internship_information.html')


def job_group(request):
    return render(request,'app/job-groups.html')


def job_record(request):
    return render(request,'app/job-records.html')


def report(request):
    return render(request,'app/report.html')


def semester(request):
    return render(request,'app/semester.html')


def student(request):
    return render(request,'app/students.html')


def faculty(request):
    return render(request, 'app/users-faculty.html')


def staff(request):
    return render(request, 'app/users-staff.html')

class SemesterView(ListView):
    model = Semester_registered
    template_name = 'app/semesters.html'