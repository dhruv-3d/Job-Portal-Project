from django.contrib import admin
from jportal.models import Category, SubCategory, Education, Employer, JobSeekers,Job

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
class JobAdmin(admin.ModelAdmin):
    list_dispaly = ('title', 'posted_date','category','sub_category','state','city')

admin.site.register(Category)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Education)
admin.site.register(Employer)
admin.site.register(JobSeekers)
admin.site.register(Job,JobAdmin)