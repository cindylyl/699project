from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('welcome/')
            else:
                return HttpResponse('Your account is inactive.')
        # Return a 'disabled account' error message
        else:
            return HttpResponse('invalid login')
        # Return an 'invalid login' error message.
    else:
        return render(request,'app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('/app')


def welcome(request):
    return render(request,'app/welcome.html')



def contact(request):
    return render(request,'app/contact.html')


def education(request):
    return render(request, 'app/education.html')


def internship_type(request):
    return render(request, 'app/internship-type.html')


def internship_info(request):
    return render(request,'app/internship-information.html')


def job_group(request):
    return render(request,'app/job-groups.html')


def job_record(request):
    return render(request,'app/job-records.html')

def semester(request):
    return render(request,'app/semester.html')


def student(request):
    return render(request,'app/students.html')


def faculty(request):
    return render(request, 'app/users-faculty.html')


def staff(request):
    return render(request, 'app/users-staff.html')


def add_education(request):
    return render(request, 'app/education-addnew.html')


def add_internship_type(request):
    return render(request, 'app/internship-type-addnew.html')


def add_internship_info(request):
    return render(request,'app/internship-information-addnew.html')


def add_job_group(request):
    return render(request,'app/job-groups-addnew.html')


def add_job_record(request):
    return render(request,'app/job-records-addnew.html')

def add_semester(request):
    return render(request,'app/semester-addnew.html')


def add_student(request):
    return render(request,'app/students-addnew.html')


def add_faculty(request):
    return render(request, 'app/users-faculty-addnew.html')


def add_staff(request):
    return render(request, 'app/users-staff-addnew.html')


def add_semester(request):
    return render(request,'app/semesters-addnew.html')

class SemesterView(ListView):
    model = Semester_registered
    template_name = 'app/semesters.html'


def report(request):
    return render(request,'app/report.html')


