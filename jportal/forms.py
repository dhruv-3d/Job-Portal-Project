from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from jportal.models import Employer, EmployerCompanyProfile
from jportal.models import JobSeekers, JobSeekersProfile
from jportal.models import AddJob, Resume, Depend
from jportal.models import Category, SubCategory

from smart_selects.form_fields import ChainedSelect, ChainedModelChoiceField
from captcha.fields import CaptchaField
import datetime

STATES = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))

CITIES = [
    ('Surat','Surat'),
    ('Ahmedabad','Ahmedabad'),    
    ('Pune', 'Pune'),
    ('Mumbai','Mumbai'),
    ('Jaipur','Jaipur'),
]

GENDER = [
    ('male','Male'), ('female','Female'),
]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    username = ''

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password',)

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')

class EmployerForm(forms.ModelForm):

    state = forms.CharField(widget=forms.Select(choices=STATES), max_length=255)
    city = forms.CharField(widget=forms.Select(choices=CITIES), required=True)
    profile_img = forms.ImageField(required=False)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER), required=True)
    dob = forms.DateField(widget=forms.DateInput())
    contact_no = forms.CharField(max_length=10, required=True)
    captcha = CaptchaField()
    tc = forms.BooleanField(widget=forms.CheckboxInput(), required=True)
    admin_approval = False

    class Meta:
        model = Employer
        fields = ('state', 'city', 'profile_img', 'gender', 'dob', 'contact_no', 'captcha', 'tc',)

class EmployerEditForm(forms.ModelForm):
    state = forms.CharField(widget=forms.Select(choices=STATES), max_length=255)
    city = forms.CharField(widget=forms.Select(choices=CITIES), required=True)
    profile_img = forms.ImageField(required=False)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER), required=True)
    dob = forms.DateField(widget=forms.DateInput())
    contact_no = forms.CharField(max_length=10, required=True)
    class Meta:
        model = Employer
        fields = ('state', 'city', 'profile_img', 'gender', 'dob', 'contact_no',) 

class EmployerCompanyProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerCompanyProfile
        exclude = ('employer','logo',)

class JobSeekerForm(forms.ModelForm):
        
    state = forms.CharField(widget=forms.Select(choices=STATES), required=True)
    city = forms.CharField(widget=forms.Select(choices=CITIES), required=True)
    profile_img = forms.ImageField(required=False)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER), required=True)
    dob = forms.SelectDateWidget()
    contact_no = forms.CharField(max_length=10, required=True)
    captcha = CaptchaField()
    tc = forms.BooleanField(widget=forms.CheckboxInput(), required=True)
    phone_verify = False
    
    class Meta:
        model = JobSeekers
        fields = ('state', 'city', 'profile_img', 'gender', 'dob', 'contact_no', 'captcha', 'tc',)

class SearchForm(forms.ModelForm):
    class Meta:
        model = Depend
        exclude = ('id',)

#------
#karishma's form
class JobForm(forms.ModelForm):
    class Meta:
       model = AddJob
       exclude = ('posted_date','employer','slug',)

class ResumeForm(forms.ModelForm):
    preffered_job_location = forms.CharField(widget=forms.Select(choices=CITIES),required=True)
    state = forms.CharField(widget=forms.Select(choices=STATES),required=True)
    city = forms.CharField(widget=forms.Select(choices=CITIES),required=True)
    class Meta:
        model = Resume
        fields = ('resumetitle','preffered_job_location','state','city','category','subcategory','totalexp','currentsalary',)