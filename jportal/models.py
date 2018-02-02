from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from django.template.defaultfilters import slugify

class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return self.name

class Education(models.Model):
    education = models.CharField(max_length=100)


class Employer(models.Model):
    user = models.ForeignKey(User)
    state = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    profile_img = models.ImageField(blank=True, upload_to='employer_pic')
    gender = models.CharField(max_length=10, blank=False)
    dob = models.DateField(blank=True)
    con_no = models.CharField(max_length=10, blank=False)
    email_verify = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class EmployerProfile(models.Model):
    employer = models.ForeignKey(Employer)
    company_name = models.CharField(max_length=150,blank=False)
    description = models.TextField(blank=True)
    address = models.TextField(blank=False)
    logo = models.ImageField(blank=True)

    def __str__(self):
        return self.company_name

class JobSeekers(models.Model):
    user = models.ForeignKey(User)
    state = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    profile_img = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, blank=False)
    dob = models.DateField(blank=True)
    con_no = models.CharField(max_length=10, blank=False)
    email_verify = models.BooleanField(default=False)
    phone_verify = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class  JobSeekersProfile(models.Model):
    user = models.OneToOneField(JobSeekers)
    pref_job_loc = models.CharField(max_length=100, blank=True)
    resume = models.FileField(blank=True)
    category = models.CharField(max_length=50, blank=True)
    sub_category = models.CharField(max_length=50, blank=True)
    education =  models.CharField(max_length=50, blank=True)
    key_skills = models.TextField(blank=False)
    total_workexp = models.DateTimeField(blank=False)
    current_drawn_sal = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.user.username

class Job(models.Model):
    employer = models.ForeignKey(Employer)
    title = models.CharField(max_length=100, blank=False)
    posted_date = models.DateField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    last_date = models.DateField(blank=False)
    salary = models.PositiveIntegerField(blank=True)
    Job_responsibility = models.TextField(blank=False)
    candidate_profile = models.TextField(blank=False)

    def __str__(self):
        return self.title

class Appliers(models.Model):
    applier = models.ForeignKey(JobSeekers)
    job_id = models.ForeignKey(Job)
    date_apply = models.DateField()
    status = models.CharField(max_length=50)

class AddJob(models.Model):
    category=models.ForeignKey(Category)
    subcategory= ChainedForeignKey(
        SubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True)
    title=models.CharField(max_length=100,blank=False,unique=True)
    employer = models.ForeignKey(Employer)
    last_date = models.DateField(blank=True)
    salary = models.PositiveIntegerField(blank=True)
    Job_responsibility = models.TextField(blank=False)
    candidate_profile = models.TextField(blank=False)
    posted_date= models.DateTimeField(auto_now=True, blank=True)
    slug=models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) 
        super(AddJob, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Resume(models.Model):
    resumetitle = models.CharField(max_length=120,blank=False)
    preffered_job_location = models.CharField(max_length=120,blank=False)
    state = models.CharField(max_length=120,blank=False)
    city = models.CharField(max_length=120,blank=False)
    category = models.ForeignKey(Category)
    subcategory= ChainedForeignKey(
        SubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True)
    totalexp = models.TextField(blank=False)
    currentsalary = models.PositiveIntegerField(blank=False)
    jobseeker = models.ForeignKey(JobSeekers)

    def __str__(self):
        return self.resumetitle