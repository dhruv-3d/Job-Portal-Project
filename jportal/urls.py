from django.conf.urls import url 
from jportal import views
from django.shortcuts import render


urlpatterns = [
    url(r'^$', views.index, name='index'), #common

    # for registration
    url(r'^regsiter/$', views.register, name='register'), #common
    url(r'^employer_register/$', views.employer_reg, name='employer_register'), #common
    url(r'^jobseeker_register/$', views.jobseeker_reg, name='jobseeker_register'), #common
    
    url(r'^jobseeker_edit/$',views.jobseeker_edit,name='jobseeker_edit'), #j
    url(r'^resume/$',views.resume,name='resume'), #j
    
    #employer links----
    url(r'^employer_profile/(?P<username>[\w\@\.]+)/$', views.employer_profile, name='employer_profile'), #e
    url(r'^emp_edit/(?P<username>[\w\@\.]+)/$', views.edit_employer_profile, name='emp_edit'), #e
    url(r'^company_edit/$', views.edit_company_details, name='company_edit'), #e

    #links related to jobs-----
    url(r'^add_job/$',views.add_job,name='add_job'), #e
    url(r'^managejob/$',views.manage_job,name='managejob'), #e
    url(r'^job_listing/',views.job_listing,name='job_listing'), #common
    url(r'^edit_job/(?P<addjob_title_slug>[\w\-]+)/$',views.edit_job,name='edit_job'), #e
    url(r'^(?P<addjob_title_slug>[\w\-]+)/delete_job/$',views.delete_job,name='delete_job'), #e
    url(r'^job_details/(?P<jobslug_name>[\w\-]+)/$',views.job_details,name='job_details'), #common
    url(r'^job_apply/(?P<jobslug_name>[\w\-]+)/$',views.job_apply, name='job_apply'), #j
    url(r'^jobs_applied/$',views.jobs_applied, name='jobs_applied'), #j

    # is idle---can be used!
    #url(r'^employer_page/$', views.employer_page, name='employer_page'),
    url(r'^jobseeker_page/$', views.jobseeker_page, name='jobseeker_page'),
    #url(r'^detail_employer/$', views.detail_employer, name='detail_employer'),
]