from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^contact$', views.contact,name='contact'),
    url(r'^education/$', views.education,name='education'),
    url(r'^internship_info$', views.internship_info,name='internship_info'),
    url(r'^internship_type$', views.internship_type,name='internship_type'),
    url(r'^job_record$', views.job_record,name='job_record'),
    url(r'^job_group$', views.job_group,name='job_group'),
    url(r'^student$', views.student,name='student'),
    url(r'^faculty$', views.faculty, name='faculty'),
    url(r'^staff$',views.staff,name='staff'),
    url(r'^semester$',views.SemesterView.as_view(),name='semester'),
    url(r'^add_education/$', views.add_education, name='add_education'),
    url(r'^add_internship_info$', views.add_internship_info, name='add_internship_info'),
    url(r'^add_internship_type$', views.add_internship_type, name='add_internship_type'),
    url(r'^add_job_record$', views.add_job_record, name='add_job_record'),
    url(r'^add_job_group$', views.add_job_group, name='add_job_group'),
    url(r'^add_student$', views.add_student, name='add_student'),
    url(r'^add_faculty$', views.add_faculty, name='add_faculty'),
    url(r'^add_staff$', views.add_staff, name='add_staff'),
    url(r'^add_semester$', views.add_semester, name='add_semester'),
    url(r'^report$',views.report, name="report"),
    url(r'logout/',views.user_logout, name='logout'),
]