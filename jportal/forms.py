from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from jportal.models import Employer, EmployerCompanyProfile, AddJob
from jportal.models import JobSeekers, JobSeekersProfile
from jportal.models import Category, SubCategory, State, City, Education
from jportal.models import Graduation, Post_Graduation, PhD, Search

from smart_selects.form_fields import ChainedSelect, ChainedModelChoiceField
from captcha.fields import CaptchaField
import datetime

GENDER = [
    ('Male','Male'), ('Female','Female'),
]
GRADING_SYSTEM = [
    ('1','Select'), ('2','Scale 10 Grading System'), ('3','Scale 4 Grading System'), 
    ('4', '% Marks of 100 Maximum'), ('5', 'Course Requires a Pass')
]

def get_years(initial=1970):
    return [(year, year) for year in range(datetime.datetime.now().year, initial, -1)]
    
class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput,required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    username = ''

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'password', 'confirm_password',)

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')

class EmployerForm(forms.ModelForm):
    designation = forms.CharField(max_length=30,required=True)
    company_name = forms.CharField(max_length=30,required=True )
    profile_img = forms.ImageField(required=False)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER), required=True)
    dob = forms.DateField(widget=forms.DateInput(),help_text='MM/DD/YYYY')
    captcha = CaptchaField()
    tc = forms.BooleanField(widget=forms.CheckboxInput(), required=True)
    admin_approval = False

    class Meta:
        model = Employer
        fields = ('designation','company_name','state', 'city', 'profile_img', 'gender', 'dob', 'contact_no', 'captcha', 'tc',)

class EmployerEditForm(forms.ModelForm):
    designation = forms.CharField(max_length=30,required=True)
    company_name = forms.CharField(max_length=30,required=True )
    profile_img = forms.ImageField(required=False)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER), required=True)
    dob = forms.DateField(widget=forms.DateInput(),help_text='MM/DD/YYYY')
    class Meta:
        model = Employer
        fields = ('designation','company_name','state', 'city', 'profile_img', 'gender', 'dob', 'contact_no',)    

class EmployerCompanyProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerCompanyProfile
        exclude = ('employer',)

class JobSeekerForm(forms.ModelForm):
    profile_img = forms.ImageField(required=False)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER), required=True)
    dob = forms.DateField(widget=forms.DateInput(),help_text='MM/DD/YYYY')
    captcha = CaptchaField()
    tc = forms.BooleanField(widget=forms.CheckboxInput(), required=True)

    class Meta:
        model = JobSeekers
        fields = ('gender','state', 'city','profile_img', 'dob', 'contact_no', 'captcha', 'tc',)
class JobSeekerEditForm(forms.ModelForm):
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER), required=True)
    dob = forms.DateField(widget=forms.DateInput(),help_text='MM/DD/YYYY')
    class Meta:
        model = JobSeekers
        fields = ('gender','state', 'city', 'profile_img', 'dob', 'contact_no')
class JobseekerprofileForm(forms.ModelForm):
    class Meta:
       model = JobSeekersProfile
       exclude = ('jobseeker','resume',)



class SearchByCategory(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('category','subcategory')


#------
#karishma's form
class JobForm(forms.ModelForm):
    class Meta:
       model = AddJob
       exclude = ('posted_date','employer','slug','state','city')


class GraduationForm(forms.ModelForm):
    graduation = forms.ModelChoiceField(queryset=Graduation.objects.all(), required=True)
    specialization = forms.CharField(max_length=50,required=True)
    university = forms.CharField(max_length=200,required=True)
    year = forms.ChoiceField(choices=get_years(),required=True)
    grading_system = forms.ChoiceField(choices=GRADING_SYSTEM)
    marks = forms.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        model = Education
        fields = ('graduation','specialization','university','year','grading_system','marks',)

class PostGraduationForm(forms.ModelForm):
    post_graduation = forms.ModelChoiceField(queryset=Post_Graduation.objects.all(), required=True)
    specialization = forms.CharField(max_length=50,required=True)
    university = forms.CharField(max_length=200,required=True)
    year = forms.ChoiceField(choices=get_years(),required=True)
    grading_system = forms.ChoiceField(choices=GRADING_SYSTEM)
    marks = forms.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        model = Education
        fields = ('post_graduation','specialization','university','year','grading_system','marks',)

class PhDForm(forms.ModelForm):
    phd = forms.ModelChoiceField(queryset=PhD.objects.all(), required=True)
    specialization = forms.CharField(max_length=50,required=True)
    university = forms.CharField(max_length=200,required=True)
    year = forms.ChoiceField(choices=get_years(),required=True)
    grading_system = forms.ChoiceField(choices=GRADING_SYSTEM)
    marks = forms.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        model = Education
        fields = ('phd','specialization','university','year','grading_system','marks',)

class ClassXIIForm(forms.ModelForm):
    board = forms.CharField(max_length=50,required=True)
    year = forms.ChoiceField(choices=get_years(),required=True)
    medium = forms.CharField(max_length=50,required=True)
    percentage = forms.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        model = Education
        fields = ('board','year','medium','percentage',)

class ClassXForm(forms.ModelForm):
    board = forms.CharField(max_length=50,required=True)
    year = forms.ChoiceField(choices=get_years(),required=True)
    medium = forms.CharField(max_length=50,required=True)
    percentage = forms.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        model = Education
        fields = ('board','year','medium','percentage',)
    
class SearchByLocation(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('state','city')

class UploadResume(forms.ModelForm):
    class Meta:
        model = JobSeekersProfile
        fields = ('resume',)
