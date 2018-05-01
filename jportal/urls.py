from django.conf.urls import url 
from jportal import views
from django.shortcuts import render


urlpatterns = [
    url(r'^$', views.index, name='index'), #common
    url(r'^jobsbycities/(?P<city_id>[\d]+)/$', views.banner_city, name='banner_city'),
    url(r'^jobsbycategory/(?P<cat_id>[\d]+)/$', views.banner_cat, name='banner_cat'),
    # Common
    url(r'^regsiter/$', views.register, name='register'), #common
    url(r'^employer_register/$', views.employer_reg, name='employer_register'), #common
    url(r'^jobseeker_register/$', views.jobseeker_reg, name='jobseeker_register'), #common
    url(r'^services/$', views.services, name='services'), #common   
    url(r'^about/$', views.about, name='about'), #common
    url(r'^contact/$', views.contact, name='contact'), #common
    url(r'^chat/$', views.chat, name='chat'), #common

    #jobseekers
    url(r'^(?P<username>[\w\@\.]+)/jobseeker_profile/$', views.jobseeker_profile, name='jobseeker_profile'),
    url(r'^(?P<username>[\w\@\.]+)/jobseeker_edit/$',views.jobseeker_edit,name='jobseeker_edit'),
    url(r'^(?P<username>[\w\@\.]+)/create_resume/$', views.create_resume, name='resume'),
    url(r'^(?P<username>[\w\@\.]+)/view_resume/$', views.view_resume, name='view_resume'),
    #education---
    url(r'^(?P<username>[\w\@\.]+)/education/$',views.add_education,name='education'),
    url(r'^(?P<username>[\w\@\.]+)/graduation/$',views.add_grad,name='graduation'),
    url(r'^(?P<username>[\w\@\.]+)/post_graduation/$',views.add_postgrad,name='post_graduation'),
    url(r'^(?P<username>[\w\@\.]+)/phd/$',views.add_doctorate,name='phd'),
    url(r'^(?P<username>[\w\@\.]+)/class_xii/$',views.add_classxii,name='class_xii'),
    url(r'^(?P<username>[\w\@\.]+)/class_x/$',views.add_classx,name='class_x'),
    #employer links----
    url(r'^employer_profile/(?P<username>[\w\@\.]+)/$', views.employer_profile, name='employer_profile'), #e
    url(r'^emp_edit/(?P<username>[\w\@\.]+)/$', views.edit_employer_profile, name='emp_edit'), #e
    url(r'^company_edit/$', views.edit_company_details, name='company_edit'), #e
    url(r'^(?P<username>[\w\@\.]+)/search_jobseeker/$', views.search, name='search_jobseeker'), #e
    url(r'^search_jobseeker/(?P<user_id>[\d]+)/save/$', views.save_seek, name='save_jobseeker'), #e
    url(r'^(?P<username>[\w\@\.]+)/saved_jobseekers/$', views.saved_jobseekers, name='saved_jobseekers'), #e
    url(r'^(?P<emp_username>[\w\@\.]+)/view_jobseeker/(?P<username>[\w\@\.]+)/$', views.view_jobseeker, name='view_jobseeker'),
    url(r'^job_approval/$', views.job_approval, name='job_approval'), #e

    #links related to jobs-----
    url(r'^add_job/$',views.add_job,name='add_job'), #e
    url(r'^managejob/$',views.manage_job,name='managejob'), #e
    url(r'^job_listing/',views.job_listing,name='job_listing'), #common
    url(r'^edit_job/(?P<addjob_title_slug>[\w\-]+)/$',views.edit_job,name='edit_job'), #e
    url(r'^(?P<addjob_title_slug>[\w\-]+)/delete_job/$',views.delete_job,name='delete_job'), #e
    url(r'^job_details/(?P<jobslug_name>[\w\-]+)/$',views.job_details,name='job_details'), #common
    url(r'^job_apply/(?P<jobslug_name>[\w\-]+)/$',views.job_apply, name='job_apply'), #j
    url(r'^jobs_applied/$',views.jobs_applied, name='jobs_applied'), #j
    url(r'^job_applications/$',views.job_applications, name='job_applications'), #e
    url(r'^search_job/$',views.search_job, name='search_job'), #j
    url(r'^recomm_job/$',views.recomm_job, name='recomm_job'), #j

]
