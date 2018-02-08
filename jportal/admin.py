from django.contrib import admin
from jportal.models import Category, SubCategory, Employer, JobSeekers,AddJob, State, City
from jportal.models import Graduation, Post_Graduation, PhD

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
class JobAdmin(admin.ModelAdmin):
    list_dispaly = ('title', 'posted_date','category','sub_category','state','city')
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')

admin.site.register(Category)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Employer)
admin.site.register(JobSeekers)
admin.site.register(AddJob,JobAdmin)
admin.site.register(State)
admin.site.register(City,CitiesAdmin)
admin.site.register(Graduation)
admin.site.register(Post_Graduation)
admin.site.register(PhD)