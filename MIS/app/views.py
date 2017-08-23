from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction

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

# django object CRUD operation:
# use CreateView, UpdateView, DeleteView
# https://rayed.com/wordpress/?p=1266


def education(request):
    education_list = Education.objects.all()
    return render(request, 'app/education.html',{'education_list': education_list})

class EducationCreateView(CreateView):
    model = Education
    fields = '__all__'
    # template_name = 'app/education-form.html'
    success_url = reverse_lazy('app:education')

class EducationUpdateView(UpdateView):
    model = Education
    fields = '__all__'
    # template_name = 'app/education-form.html'
    success_url = reverse_lazy('app:education')


class EducationDeleteView(DeleteView):
    model = Education
    success_url = reverse_lazy('app:education')



def internship_type(request):
    internshiptype = Internship.objects.all()
    type = Internship.objects.get(intern_type='MAC Project')

    return render(request, 'app/internship-type.html',{'internshiptype':internshiptype})


def internship_info(request):
    return render(request,'app/internship-information.html')


# class InternshipInfoView(LoginRequiredMixin,View):
#     def get(self,request,*args,**kwargs):
#         info = get_object_or_404(Intern_Info, id=kwargs['id'])
#         return render(request,)
#
#     def post(self,request,*args,**kwargs):
#         pass


class InternshipInfoListView(ListView):
    model = Intern_Info
    template_name = 'app/internship-information.html'
    context_object_name = 'info_list'

class InternshipInfoCreateView(CreateView):
    model = Intern_Info
    fields = '__all__'
    template_name = 'app/internship-information-form.html'
    success_url = reverse_lazy('app:internship_info')

class InternshipInfoUpdateView(UpdateView):
    model = Intern_Info
    fields = '__all__'
    template_name = 'app/internship-information-form.html'
    success_url = reverse_lazy('app:internship_info')


class InternshipInfoDeleteView(DeleteView):
    model = Intern_Info
    success_url = reverse_lazy('app:internship_info')

def job_group(request):
    job_group_list = Job_groups.objects.all()
    return render(request,'app/job-groups.html',{'job_group_list':job_group_list})


class JobGroupCreateView(CreateView):
    model = Job_groups
    fields = '__all__'
    template_name = 'app/job-groups-addnew.html'
    success_url = reverse_lazy('app:job_group')



def job_record(request):
    job_record_list =Job.objects.all()
    return render(request,'app/job-records.html',{'job_record_list':job_record_list})

class JobRecordCreateView(CreateView):
    model = Job
    fields = '__all__'
    template_name = 'app/internship-information-form.html'
    success_url = reverse_lazy('app:job_record')

class JobRecordUpdateView(UpdateView):
    model = Job
    fields = '__all__'
    template_name = 'app/internship-information-form.html'
    success_url = reverse_lazy('app:job_record')


class JobRecordDeleteView(DeleteView):
    model = Job
    success_url = reverse_lazy('app:job_record')

def semester(request):
    return render(request,'app/semester.html')


def student(request):
    student_list = Student.objects.all()
    return render(request,'app/students.html',{'student_list':student_list})


class StudentCreateView(CreateView):
    model = User
    #fields = ['groups']
    template_name = 'app/students-form.html'
    success_url = reverse_lazy('app:student')
    form_class = UserForm

    def get_context_data(self, **kwargs):
        # defaultly, only return fields in User Object, here we need fields in Student Object
        data = super(StudentCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['students'] = StudentFormSet(self.request.POST)
        else:
            data['students'] = StudentFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        students = context['students']
        print(form.cleaned_data)
        with transaction.atomic():
            self.object = form.save()
            # add group attribute
            self.object.groups.clear()
            self.object.groups.add(form.cleaned_data['groups'])

            if students.is_valid():
                students.instance = self.object
                #students.group=self.cleaned_data["groups"]
                students.save()
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'app/students-form.html'
    success_url = reverse_lazy('app:student')
    context_object_name = 'stu'

    def get_context_data(self, **kwargs):
        data = super(StudentUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            data['students'] = StudentFormSet(self.request.POST,instance=self.object)
        else:
            data['students'] = StudentFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        students = context['students']
        with transaction.atomic():
            self.object = form.save()
            if students.is_valid():
                students.instance = self.object
                students.save()
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = User
    template_name = 'app/student_confirm_delete.html'
    success_url = reverse_lazy('app:student')


def faculty(request):
    faculty_list = Faculty.objects.all()
    return render(request, 'app/faculty.html',{'faculty_list':faculty_list})


class FacultyCreateView(CreateView):
    model = User
    #fields = ['username','password''first_name','last_name','email','groups']
    template_name = 'app/faculty_form.html'
    success_url = reverse_lazy('app:faculty')
    form_class = UserForm

    def get_context_data(self, **kwargs):
        data = super(FacultyCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['faculties'] = FacultyFormSet(self.request.POST)
        else:
            data['faculties'] = FacultyFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        faculties = context['faculties']

        with transaction.atomic():
            self.object = form.save()
            self.object.groups.clear()
            self.object.groups.add(form.cleaned_data['groups'])
            if faculties.is_valid():
                faculties.instance = self.object
                faculties.save()
        return super(FacultyCreateView, self).form_valid(form)


class FacultyUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'app/faculty_form.html'
    success_url = reverse_lazy('app:faculty')
    context_object_name = 'fac'

    def get_context_data(self, **kwargs):
        data = super(FacultyUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            data['faculties'] = FacultyFormSet(self.request.POST,instance=self.object)
        else:
            data['faculties'] = FacultyFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        students = context['faculties']
        with transaction.atomic():
            self.object = form.save()
            if students.is_valid():
                students.instance = self.object
                students.save()
        return super(FacultyUpdateView, self).form_valid(form)


class FacultyDeleteView(DeleteView):
    model = User
    template_name = 'app/faculty_confirm_delete.html'
    success_url = reverse_lazy('app:faculty')




def staff(request):
    staff_list = Staff.objects.all()
    return render(request, 'app/staff.html',{"staff_list":staff_list})


class StaffCreateView(CreateView):
    model = User
    #fields = ['username','password''first_name','last_name','email','groups']
    template_name = 'app/staff_form.html'
    success_url = reverse_lazy('app:staff')
    form_class = UserForm

    def get_context_data(self, **kwargs):
        data = super(StaffCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['staff'] = StaffFormSet(self.request.POST)
        else:
            data['staff'] = StaffFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        faculties = context['staff']

        with transaction.atomic():
            self.object = form.save()
            self.object.groups.clear()
            self.object.groups.add(form.cleaned_data['groups'])
            if faculties.is_valid():
                faculties.instance = self.object
                faculties.save()
        return super(StaffCreateView, self).form_valid(form)


class StaffUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'app/staff_form.html'
    success_url = reverse_lazy('app:staff')
    context_object_name = 'sta'

    def get_context_data(self, **kwargs):
        data = super(StaffUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            data['staff'] = StaffFormSet(self.request.POST,instance=self.object)
        else:
            data['staff'] = StaffFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        staff = context['staff']
        with transaction.atomic():
            self.object = form.save()
            if staff.is_valid():
                staff.instance = self.object
                staff.save()
        return super(StaffUpdateView, self).form_valid(form)


class StaffDeleteView(DeleteView):
    model = User
    template_name = 'app/staff_confirm_delete.html'
    success_url = reverse_lazy('app:staff')


def add_education(request):
    if request.method == 'POST':
        # create a form instance;  populate with data from the request:
        form =EducationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('/thanks/')
    # if a GET (or any other method) create a blank form
    else:
        form = EducationForm()
    return render(request, 'app/education_form.html',{'form':form})





def add_staff(request):
    return render(request, 'app/staff_form.html')


# def add_semester(request):
#     return render(request,'app/semesters-addnew.html')

class SemesterView(ListView):
    model = Semester_registered
    template_name = 'app/semesters.html'

class SemesterCreateView(CreateView):
    model = Semester_registered
    fields = '__all__'
    template_name = 'app/semesters-addnew.html'
    success_url = reverse_lazy('app:semester')

def report(request):
    return render(request,'app/report.html')


