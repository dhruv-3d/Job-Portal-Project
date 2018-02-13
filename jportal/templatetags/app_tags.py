from django import template

from jportal.models import Category, SubCategory, User
from jportal.models import JobSeekers, Employer, AddJob

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