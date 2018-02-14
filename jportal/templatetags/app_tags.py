from django import template

from jportal.models import Category, SubCategory, User
from jportal.models import JobSeekers, Employer, AddJob, Appliers

register = template.Library()

@register.assignment_tag
def get_emp(AddJob):
    job = AddJob

    employer = Employer.objects.get(id=job.employer_id)
    user = User.objects.get(id=employer.user_id)

    return user.username

@register.assignment_tag
def get_cat_subcat(subcat, cat):
    cat_name = Category.objects.get(id=cat)
    subcat_name = SubCategory.objects.get(id=subcat)

    return subcat_name.name + ',' + cat_name.title

@register.assignment_tag
def get_app_count(jobid):

    app_no = Appliers.objects.filter(job_id=jobid).count()

    return app_no

@register.assignment_tag
def has_app(job):

    application = Appliers.objects.filter(job_id=job.id)

    count = application.count()

    return application

@register.assignment_tag
def get_appliers(Appliers):    
    app = Appliers

    applier = JobSeekers.objects.get(id=app.jobseeker_id)
    app_user = User.objects.get(id=applier.user_id)

    return app_user.username



