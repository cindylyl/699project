from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^welcome$', views.welcome, name='welcome'),
    url(r'^contact$', views.contact,name='contact'),
    url(r'^education$', views.education,name='education'),
    url(r'^internship_info$', views.internship_info,name='internship_info'),
    url(r'^internship_type$', views.internship_type,name='internship_type'),
    url(r'^job_record$', views.job_record,name='job_record'),
    url(r'^job_group$', views.job_group,name='job_group'),
    url(r'^student$', views.student,name='student'),
    url(r'^faculty$', views.faculty, name='faculty'),
    url(r'^staff$',views.staff,name='staff'),
    url(r'^report$',views.report, name="report"),
    url(r'^semester$',views.SemesterView.as_view(),name='semester')
]