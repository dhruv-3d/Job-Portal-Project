from django.contrib import admin
from jportal.models import Category, SubCategory, Education, Employer, JobSeekers

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Education)
admin.site.register(Employer)
admin.site.register(JobSeekers)
