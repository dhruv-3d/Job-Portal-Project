from django.conf.urls import url 
from jportal import views
from django.shortcuts import render


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^add_job/$',views.add_job,name='add_job'),
    url(r'^managejob/$',views.manage_job,name='managejob'),
    url(r'^(?P<addjob_title_slug>[\w\-]+)/delete_job/$',views.delete_job,name='delete_job'),
    url(r'^edit_job/(?P<addjob_title_slug>[\w\-]+)/$',views.edit_job,name='edit_job'),
    url(r'^job_listing/',views.job_listing,name='job_listing'),
    url(r'^employer_register/$', views.employer_reg, name='employer_register'),
    url(r'^jobseeker_register/$', views.jobseeker_reg, name='jobseeker_register'),
    url(r'^search_jobseeker/$',views.search_j,name='search_jobseeker'),

    url(r'^education/(?P<username>[\w\@\.]+)/$',views.add_education,name='education'),
    url(r'^employer_profile/(?P<username>[\w\@\.]+)/$', views.employer_profile, name='employer_profile'),
    url(r'^jobseeker_profile/(?P<username>[\w\@\.]+)/$', views.jobseeker_profile, name='jobseeker_profile'),
    url(r'^jobseek_pro/$', views.jobseekpro, name='jobseek_pro'),
    url(r'^emp_edit/(?P<username>[\w\@\.]+)/$', views.edit_employer_profile, name='emp_edit'),
    url(r'^company_edit/$', views.edit_company_details, name='company_edit'),
    url(r'^job_applications/$',views.job_applications, name='job_applications'),
]