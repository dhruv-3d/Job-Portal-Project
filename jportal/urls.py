from django.conf.urls import url 
from jportal import views
from django.shortcuts import render


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^job/$',views.add_job,name='job'),
    url(r'^managejob/$',views.manage_job,name='managejob'),
    url(r'^job_listing/',views.job_listing,name='job_listing'),

    url(r'^employer_register/$', views.employer_reg, name='employer_register'),
    url(r'^jobseeker_register/$', views.jobseeker_reg, name='jobseeker_register'),

    url(r'^employer_page/$', views.employer_page, name='employer_page'),
    url(r'^detail_employer/$', views.detail_employer, name='detail_employer'),
    url(r'^employer_profile/(?P<username>[\w\@\.]+)/$', views.employer_profile, name='employer_profile'),
]