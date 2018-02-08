from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import MaxValueValidator
class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return self.name
class Graduation(models.Model):
    title = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Graduation'

    def __str__(self):
        return self.title

class Post_Graduation(models.Model):
    title = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Post Graduation'

    def __str__(self):
        return self.title
    
class PhD(models.Model):
    title = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'PhD'
    def __str__(self):
        return self.title

class Education(models.Model):
    graduation = models.ForeignKey(Graduation,on_delete=models.SET_NULL,blank=True,null=True)
    post_graduation = models.ForeignKey(Post_Graduation,on_delete=models.SET_NULL,blank=True,null=True)
    phd = models.ForeignKey(PhD,on_delete=models.SET_NULL,blank=True,null=True)
    specialization = models.CharField(max_length=50,blank=True)
    university = models.CharField(max_length=200,blank=True)
    year = models.CharField(max_length=10,blank=True)
    grading_system = models.CharField(max_length=50,blank=True)
    marks = models.DecimalField(max_digits=2,decimal_places=2,default=0,blank=True)
    school = models.CharField(max_length=200,blank=True)
    board = models.CharField(max_length=10,blank=True)
    medium = models.CharField(max_length=20,blank=True)
    percentage = models.DecimalField(max_digits=2,decimal_places=2,default=0,blank=True)
    class Meta:
        verbose_name_plural = 'PhD'

class State(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Cities'
    def __str__(self):
        return self.name

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30, blank=False)
    company_name = models.CharField(max_length=150,blank=False)
    state = models.ForeignKey(State,on_delete=models.SET_NULL, null=True,blank=False)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True,blank=False)
    profile_img = models.ImageField(blank=True, upload_to='employer_pic')
    gender = models.CharField(max_length=10, blank=False)
    dob = models.DateField(blank=True)
    contact_no = models.PositiveIntegerField(blank=False,validators=[MaxValueValidator(9999999999)])
    email_verify = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class EmployerCompanyProfile(models.Model):
    employer = models.OneToOneField(Employer,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150,blank=False)
    description = models.TextField(blank=True)
    address = models.TextField(blank=False)
    logo = models.ImageField(blank=True, upload_to='company_logo')

    def __str__(self):
        return self.company_name

class JobSeekers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.SET_NULL, null=True, blank=False)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=False)
    profile_img = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, blank=False)
    dob = models.DateField(blank=True)
    contact_no = models.PositiveIntegerField(blank=False,validators=[MaxValueValidator(9999999999)])
    email_verify = models.BooleanField(default=False)
    phone_verify = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = 'JobSeekers'
    def __str__(self):
        return self.user.username

class AddJob(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory= ChainedForeignKey(
        SubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True)
    title=models.CharField(max_length=100,blank=False)
    employer = models.ForeignKey(Employer,on_delete=models.CASCADE)
    last_date = models.DateField(blank=True)
    salary = models.PositiveIntegerField(blank=True)
    Job_responsibility = models.TextField(blank=False)
    candidate_profile = models.TextField(blank=False)
    posted_date= models.DateTimeField(auto_now=True)

class Appliers(models.Model):
    applier = models.ForeignKey(JobSeekers,on_delete=models.CASCADE)
    job_id = models.ForeignKey(AddJob,on_delete=models.CASCADE)
    date_apply = models.DateField()
    status = models.CharField(max_length=50)

class JobSeekersProfile(models.Model):
    user = models.OneToOneField(JobSeekers,on_delete=models.CASCADE)
    pref_job_loc = models.CharField(max_length=100, blank=True)
    resume = models.FileField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    subcategory= ChainedForeignKey(
        SubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True)
    education =  models.ForeignKey(Education,on_delete=models.SET_NULL, null=True)
    key_skills = models.TextField(blank=False)
    total_workexp = models.DateTimeField(blank=False)
    current_drawn_sal = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.user.username