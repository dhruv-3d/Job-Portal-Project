from django.conf.urls import url 
from jportal import views
from django.shortcuts import render


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^add_job/$',views.add_job,name='add_job'),
    url(r'^managejob/$',views.manage_job,name='managejob'),

    url(r'^employer_register/$', views.employer_reg, name='employer_register'),
    url(r'^jobseeker_register/$', views.jobseeker_reg, name='jobseeker_register'),
    url(r'^(?P<username>[\w\@\.]+)/education/$',views.add_education,name='education'),
    url(r'^(?P<username>[\w\@\.]+)/graduation/$',views.add_grad,name='graduation'),
    url(r'^(?P<username>[\w\@\.]+)/post_graduation/$',views.add_postgrad,name='post_graduation'),
    url(r'^(?P<username>[\w\@\.]+)/phd/$',views.add_doctorate,name='phd'),
    url(r'^(?P<username>[\w\@\.]+)/class_xii/$',views.add_classxii,name='class_xii'),
    url(r'^(?P<username>[\w\@\.]+)/class_x/$',views.add_classx,name='class_x'),
    url(r'^employer_profile/$', views.employer_profile, name='employer_profile'),
    url(r'^(?P<username>[\w\@\.]+)/jobseeker_profile/$', views.jobseeker_profile, name='jobseeker_profile'),
    url(r'^emp_edit/(?P<username>[\w\@\.]+)/$', views.edit_employer_profile, name='emp_edit'),
    url(r'^company_edit/$', views.edit_company_details, name='company_edit'),
]