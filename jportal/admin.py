from django.contrib import admin
from jportal.models import Category, SubCategory, Employer, JobSeekers, AddJob, Appliers, SaveJobseeker
from jportal.models import Graduation, Post_Graduation, PhD, State, City, Banners_category,Banners_state

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

class Banners_stateAdmin(admin.ModelAdmin):
    list_display = ( 'state', 'img', 'name')

class Banners_categoryAdmin(admin.ModelAdmin):
    list_display = ('category','img','name')

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
admin.site.register(SaveJobseeker)
admin.site.register(Banners_state,Banners_stateAdmin)
admin.site.register(Banners_category,Banners_categoryAdmin)