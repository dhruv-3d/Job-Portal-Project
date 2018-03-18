from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator
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


class State(models.Model):
    state = models.CharField(max_length=100)
    def __str__(self):
        return self.state
    
class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city =models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Cities'
    def __str__(self):
        return self.city


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30, blank=False)
    company_name = models.CharField(max_length=150,blank=False)
    state = models.ForeignKey(State,on_delete=models.SET_NULL,null=True,blank=False)
    city = ChainedForeignKey(
            City,
            chained_field="state",
            chained_model_field="state",
            show_all=False,
            auto_choose=True,
            sort=True)
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.SET_NULL,null=True,blank=False)
    city = ChainedForeignKey(
            City,
            chained_field="state",
            chained_model_field="state",
            show_all=False,
            auto_choose=True,
            sort=True)
    profile_img = models.ImageField(blank=True,upload_to='jobseeker_pic')
    gender = models.CharField(max_length=10, blank=False)
    dob = models.DateField(blank=True)
    contact_no = models.CharField(max_length=10, blank=False)
    email_verify = models.BooleanField(default=False)
    phone_verify = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Education(models.Model):
    jobseeker = models.ForeignKey(JobSeekers,on_delete=models.CASCADE,blank=True,null=True)
    category = models.CharField(max_length=30,blank=True,null=True)
    graduation = models.ForeignKey(Graduation,on_delete=models.SET_NULL,blank=True,null=True)
    post_graduation = models.ForeignKey(Post_Graduation,on_delete=models.SET_NULL,blank=True,null=True)
    phd = models.ForeignKey(PhD,on_delete=models.SET_NULL,blank=True,null=True)
    specialization = models.CharField(max_length=50,blank=True)
    university = models.CharField(max_length=200,blank=True)
    year = models.CharField(max_length=10,blank=True)
    grading_system = models.CharField(max_length=50,blank=True)
    marks = models.DecimalField(max_digits=4,decimal_places=2,default=0,blank=True)
    school = models.CharField(max_length=200,blank=True)
    board = models.CharField(max_length=10,blank=True)
    medium = models.CharField(max_length=20,blank=True)
    percentage = models.DecimalField(max_digits=4,decimal_places=2,default=0,blank=True)
    class Meta:
        verbose_name_plural = 'Education'

class JobSeekersProfile(models.Model):
    jobseeker = models.OneToOneField(JobSeekers,on_delete=models.CASCADE)
    linkedin_profile = models.CharField(max_length=200, blank=True)
    pref_job_loc = models.CharField(max_length=100, blank=True)
    resume = models.FileField(blank=True, upload_to='resume')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    subcategory= ChainedForeignKey(
        SubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True)
    designation = models.CharField(max_length=30, blank=False, null=True)
    key_skills = models.TextField(blank=False)
    total_workexp = models.CharField(max_length=20,blank=False)
    current_drawn_sal = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.jobseeker.user.username

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
    salary = models.CharField(max_length=50,blank=True)
    Job_responsibility = models.TextField(blank=False)
    candidate_profile = models.TextField(blank=False)
    posted_date= models.DateTimeField(auto_now=True, blank=True)
    slug=models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) 
        super(AddJob, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Appliers(models.Model):
    jobseeker = models.ForeignKey(JobSeekers)
    job = models.ForeignKey(AddJob)
    date_apply = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.job

class Subscribtion(models.Model):
    sub_status = models.BooleanField(default=False)
    subscriber_email = models.EmailField()

class Newsletter(models.Model):
    sender_email = models.EmailField()
    sent_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=120, blank=False)
    message = models.CharField(max_length=500, blank=False)
    sent_to = models.CharField(max_length=2000, blank=True)

class Search(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    subcategory = ChainedForeignKey(
        SubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True)
    state = models.ForeignKey(State,on_delete=models.SET_NULL,null=True,blank=True)
    city = ChainedForeignKey(
            City,
            chained_field="state",
            chained_model_field="state",
            show_all=False,
            auto_choose=True,
            sort=True,
            blank=True)

class SaveJobseeker(models.Model):
    emp = models.ForeignKey(Employer, on_delete=models.CASCADE, blank=True)
    jobseeker = models.ForeignKey(JobSeekers, on_delete=models.CASCADE, blank=True)


class Banners_state(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True)
    img =  models.ImageField(blank=False)
    name = models.CharField(max_length=200,blank=False)

class Banners_category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    img = models.ImageField(blank=False)
    name = models.CharField(max_length=200,blank=False)


