from django.conf.urls import url 
from jportal import views
from django.shortcuts import render


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^add_job/$',views.add_job,name='add_job'),
    url(r'^managejob/$',views.manage_job,name='managejob'),
    url(r'^job_listing/',views.job_listing,name='job_listing'),
    url(r'^(?P<addjob_title_slug>[\w\-]+)/delete_job/$',views.delete_job,name='delete_job'),
    url(r'^edit_job/(?P<addjob_title_slug>[\w\-]+)/$',views.edit_job,name='edit_job'),

    url(r'^jobseeker_registration/$',views.jobseeker_reg,name='jobseeker_registration'),
    url(r'^jobseeker_edit/$',views.jobseeker_edit,name='jobseeker_edit'),

    url(r'^employer_register/$', views.employer_reg, name='employer_register'),
    url(r'^employer_page/$', views.employer_page, name='employer_page'),
    url(r'^detail_employer/$', views.detail_employer, name='detail_employer'),
    url(r'^employer_profile/$', views.employer_profile, name='employer_profile'),
]