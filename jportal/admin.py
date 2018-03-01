from django.contrib import admin
from jportal.models import Category, SubCategory, Employer, JobSeekers, AddJob, Appliers
from jportal.models import Graduation, Post_Graduation, PhD, State, City

class ApplierAdmin(admin.ModelAdmin):
    list_display = ('jobseeker', 'job', 'status', 'date_apply')

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('user','approval')

class AddJobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'posted_date', 'category', 'subcategory')
    search_fields = ('title',)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

class CitiesAdmin(admin.ModelAdmin):
    list_display = ('city', 'state')

#registered Admin Modules    
admin.site.register(Category)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(JobSeekers)
admin.site.register(AddJob, AddJobAdmin)
admin.site.register(Appliers, ApplierAdmin)
admin.site.register(State)
admin.site.register(City,CitiesAdmin)
admin.site.register(Graduation)
admin.site.register(Post_Graduation)
admin.site.register(PhD)