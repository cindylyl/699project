from django.db import models
import datetime
from django.contrib.auth.models import User



# Create your models here.

class Internship(models.Model):
    intern_type = models.CharField(max_length=50)
    intern_discription = models.CharField(max_length=100)

    def __str__(self):
        return "{} {} {}".format(self.id, self.intern_type, self.intern_discription)


class Intern_Info(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=20, default='Ontario')
    postal_code = models.CharField(max_length=10,blank=True)
    country = models.CharField(max_length=20, default='Canada')
    contact_first_name = models.CharField(max_length=50,blank=True)
    contact_last_name = models.CharField(max_length=50,blank=True)
    contact_position = models.CharField(max_length=50,blank=True)
    telephone = models.IntegerField()
    email = models.EmailField()
    company_website = models.URLField()
    notes = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.company_name


class Job_groups(models.Model):
    job_group_type = models.CharField(max_length=20)
    job_group_description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.job_group_type


class Job(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('unopened', 'Unopened'),
        ('closed', 'Closed')
    )

    intern_id = models.ForeignKey(Internship)
    company_id = models.ForeignKey(Intern_Info)
    job_group_id = models.ForeignKey(Job_groups)
    job_position = models.CharField(max_length=50)
    job_description = models.CharField(max_length=100)
    job_responsibilities = models.CharField(max_length=50)
    job_requirements = models.CharField(max_length=50)
    job_salary = models.IntegerField()
    job_status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.company_id.company_name+" ("+self.job_position+")"


class Semester_registered(models.Model):
    SEMESTER_CHOICE = (
        ('F','Fall'),
        ('W', 'Winter')
    )
    semester_name = models.CharField(max_length=1, choices=SEMESTER_CHOICE)
    semester_year = models.IntegerField()
    semester_description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.semester_year, self.semester_name,)


class Student(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    STATUS_CHOICES = (
        ('I', 'International Resident'),
        ('P', 'Permanent Resident'),
    )

    CURRENT_PAST = (
        ('C', 'Current Student'),
        ('P', 'Past Student')
    )

    user = models.OneToOneField(User)
    job_id = models.ForeignKey(Job,blank=True,null=True)
    semester_id = models.ForeignKey(Semester_registered, blank=True, null=True)
    # stu_firstname = models.CharField(max_length=50)
    # stu_midname = models.CharField(max_length=50)
    # stu_lastname = models.CharField(max_length=50)
    # stu_email = models.EmailField()
    stu_telephone = models.IntegerField(null=True, blank= True)
    stu_gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default="")
    stu_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='I')
    stu_current_past = models.CharField(max_length=1, choices=CURRENT_PAST,default="")

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Faculty(models.Model):
    user = models.OneToOneField(User)
    fac_department = models.CharField(max_length=20,default="")
    fac_hire_date = models.DateField(auto_now=True)
    fac_professor_rank = models.IntegerField(default=0)

    def __str__(self):
        return "{}, {} {}".format(self.id, self.user.first_name, self.user.last_name)


class Staff(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return "{}, {} {}".format(self.id, self.user.first_name, self.user.last_name)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Education(models.Model):
    DEGREE_CHOICES = (
        ('F', 'Undergraduate'),
        ('M', 'Graduate'),
    )
    edu_id = models.AutoField(primary_key=True)
    edu_degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    edu_degree_title = models.CharField(max_length=50)
    edu_degree_cgpa = models.CharField(max_length=2)
    edu_degree_university = models.CharField(max_length=30)
    edu_degree_location = models.CharField(max_length=30)
    edu_certification_title = models.CharField(max_length=50)
    edu_certification_body = models.CharField(max_length=200)
    stu_id = models.ForeignKey(Student)

    def __str__(self):
        return self.edu_id

