from django import forms
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


# extend UserCreateForm: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    groups = forms.ModelChoiceField(queryset=Group.objects.all(),required=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name','last_name','password1', 'password2','groups')

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.groups = self.cleaned_data["groups"]
    #     if commit:
    #         user.save()
    #     return user


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class InternshipInfoForm(forms.ModelForm):
    class Meta:
        model = Intern_Info
        fields = '__all__'




class JobGroupForm(forms.ModelForm):
    class Meta:
        model = Job_groups
        fields = '__all__'


class JobRecordForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester_registered
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
# combine User and Student object,
StudentFormSet = inlineformset_factory(User,Student,form=StudentForm,extra=1)

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

FacultyFormSet = inlineformset_factory(User,Faculty,form=FacultyForm,extra=1)

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

StaffFormSet = inlineformset_factory(User,Staff,form=StaffForm,extra=1)