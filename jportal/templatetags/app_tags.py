from django import template
from jportal.models import Category, SubCategory, User, City, State, JobSeekersProfile
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

@register.assignment_tag
def get_jobseeker(jobseeker):
    seek = jobseeker
    j_seek = JobSeekers.objects.get(id=seek.jobseeker_id)
    user = User.objects.get(id=j_seek.user_id)

    return user.username

@register.assignment_tag
def get_category(cat):
    a = cat

    seeker = JobSeekersProfile.objects.get(id=a.category_id)
    user = User.objects.get(id=seeker.user_id)

    return user.username


#----------------for search jobseeker by (category,subcategory,state,city)
@register.assignment_tag
def get_cate(catid):
    J_see = JobSeekersProfile.objects.filter(category_id=catid)
    return J_see

@register.assignment_tag
def get_subcat(subid):
    J_see = JobSeekersProfile.objects.filter(subcategory_id=subid)
    return J_see

@register.assignment_tag
def get_state(stateid):
    js = JobSeekers.objects.filter(state_id=stateid)
    return js

@register.assignment_tag
def get_city(cityid):
    js = JobSeekers.objects.filter(city_id=cityid)   
    return js
    
@register.assignment_tag
def get_profile(id):
    j = JobSeekersProfile.objects.get(jobseeker_id=id)
    return j