from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     password = request.POST['password']
    #
    #     user = authenticate(username=email, password=password)
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #
    #             return redirect('welcome/')
    #         else:
    #             return HttpResponse('Your account is inactive.')
    #     # Return a 'disabled account' error message
    #     else:
    #         return HttpResponse('invalid login')
    #     # Return an 'invalid login' error message.
    # else:
    #     return render(request,'app/index.html')
    return render(request, 'app/index.html')

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


def report_allStudent(request):
    studentlist = Student.objects.all()
    return render(request, 'app/report_allStudent.html', {'studentlist':studentlist})

def report_studentsFromCountry(request):
    if request.method == 'POST':
        countryname = request.POST['countryname']
        studentfromcountrylist = Student.objects.filter(stu_nationality=countryname)
        return render(request, 'app/report_studentsFromCountry.html', {'studentfromcountrylist':studentfromcountrylist})
    else:
        return render(request, 'app/report_studentsFromCountry.html')

def report_studentWithJob(request):
    studentwithjoblist = Student.objects.filter(job_id__intern_id__intern_type__contains='industry')
    return render(request, 'app/report_studentWithJob.html', {'studentwithjoblist':studentwithjoblist})

def report_studentWithoutJob(request):
    studentwithoutjoblist = Student.objects.exclude(job_id__intern_id__intern_type__contains = 'industry')
    return render(request, 'app/report_studentWithoutJob.html', {'studentwithoutjoblist':studentwithoutjoblist})

def report_studentWithPay(request):
    studentwithpaylist = Student.objects.filter(job_id__job_salary__regex = "[1-9]([0-9]{1,})?")
    return render(request, 'app/report_studentWithPay.html', {'studentwithpaylist':studentwithpaylist})

def report_studentWithoutPay(request):
    studentwithoutpaylist = Student.objects.filter(job_id__job_salary = 0)
    return render(request, 'app/report_studentWithoutPay.html', {'studentwithoutpaylist':studentwithoutpaylist})

def report_averageCurrentGPA(request):
    totalcurrentGPA = 0
    i = 0
    educationcurrentlist = Education.objects.filter(stu_id__stu_current_past='C')
    for education in educationcurrentlist:
        totalcurrentGPA = totalcurrentGPA + int(education.edu_degree_cgpa)
        i = i + 1
    if totalcurrentGPA ==0:
        return render(request, 'app/report_averageCurrentGPA.html')

    averageCurrentGPA = totalcurrentGPA / i
    return render(request, 'app/report_averageCurrentGPA.html', {'averageCurrentGPA':averageCurrentGPA, "studentnumber":i})

def report_averagePreviousGPA(request):
    totalPreviousGPA = 0
    i = 0
    educationPreviouslist = Education.objects.filter(stu_id__stu_current_past='P')
    for education in educationPreviouslist:
        totalPreviousGPA = totalPreviousGPA + int(education.edu_degree_cgpa)
        i = i + 1
    if totalPreviousGPA == 0:
        return render(request, 'app/report_averagePreviousGPA.html')

    averagePreviousGPA = totalPreviousGPA / i
    return render(request, 'app/report_averagePreviousGPA.html', {'averagePreviousGPA':averagePreviousGPA, "studentnumber":i})

def report_studentsAverageCurrentGPAFromCountryFromYear(request):
    totalCurrentGPA = 0
    i = 0
    if request.method == 'POST':
        countryname = request.POST['countryname']
        semestername = request.POST['semestername']
        semesteryear = request.POST['semesteryear']
        educationlist = Education.objects.filter(stu_id__stu_current_past='C').filter(stu_id__stu_nationality=countryname).filter(
            stu_id__semester_id__semester_name=semestername).filter(stu_id__semester_id__semester_year=semesteryear)
        for education in educationlist:
            totalCurrentGPA = totalCurrentGPA + int(education.edu_degree_cgpa)
            i = i + 1
        if totalCurrentGPA == 0:
            return render(request, 'app/report_studentsAverageCurrentGPAFromCountryFromYear.html')

        averageCurrentGPA = totalCurrentGPA / i
        return render(request, 'app/report_studentsAverageCurrentGPAFromCountryFromYear.html', {'averageCurrentGPA':averageCurrentGPA, 'studentnumber':i})
    else:
        return render(request, 'app/report_studentsAverageCurrentGPAFromCountryFromYear.html')

def report_studentsWithPaidFromCountryFromYear(request):
    if request.method == 'POST':
        countryname = request.POST['countryname']
        semestername = request.POST['semestername']
        semesteryear = request.POST['semesteryear']
        studentslist = Student.objects.filter(job_id__job_salary__regex="[1-9]([0-9]{1,})?").filter(stu_nationality=countryname).filter(semester_id__semester_name=semestername).filter(semester_id__semester_year=semesteryear)
        return render(request, 'app/report_studentsWithPaidFromCountryFromYear.html', {'studentslist': studentslist})
    else:
        return render(request, 'app/report_studentsWithPaidFromCountryFromYear.html')

def report_studentsWithJobFromYear(request):
    if request.method == 'POST':
        semestername = request.POST['semestername']
        semesteryear = request.POST['semesteryear']
        studentslist = Student.objects.filter(job_id__intern_id__intern_type__contains='industry').filter(semester_id__semester_name=semestername).filter(semester_id__semester_year=semesteryear)
        return render(request, 'app/report_studentsWithJobFromYear.html', {'studentslist': studentslist})
    else:
        return render(request, 'app/report_studentsWithJobFromYear.html')

def report_studentsWithoutJobFromYear(request):
    if request.method == 'POST':
        semestername = request.POST['semestername']
        semesteryear = request.POST['semesteryear']
        studentslist = Student.objects.exclude(job_id__intern_id__intern_type__contains = 'industry').filter(semester_id__semester_name=semestername).filter(semester_id__semester_year=semesteryear)
        return render(request, 'app/report_studentsWithoutJobFromYear.html', {'studentslist': studentslist})
    else:
        return render(request, 'app/report_studentsWithoutJobFromYear.html')






def report_allEmployers(request):
    employerslist = Intern_Info.objects.all().order_by("id")
    return render(request, 'app/report_allEmployers.html', {'employerslist':employerslist})

def report_employerFromCity(request):
    if request.method == 'POST':
        cityname = request.POST['cityname']
        employerslist = Intern_Info.objects.filter(city = cityname)
        return render(request, 'app/report_employerFromCity.html', {'employerslist':employerslist})
    else:
        return render(request, 'app/report_employerFromCity.html')

def report_allOpenPositions(request):
    allopenpositionslist = Job.objects.filter(job_status='open')
    return render(request, 'app/report_allOpenPositions.html', {'allopenpositionslist':allopenpositionslist})