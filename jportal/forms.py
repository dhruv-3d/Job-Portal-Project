from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



from jportal.models import Employer, EmployerProfile
from jportal.models import JobSeekers, JobSeekersProfile
from jportal.models import Job
from jportal.models import Category, SubCategory, AddJob, Resume, City, State

from captcha.fields import CaptchaField
import datetime

GENDER = [
    ('male','Male'), ('female','Female'),
]

catlist = []

cat = Category.objects.all()
for i in range(0, len(cat)):
    catlist.append((i,cat[i]))

print(catlist)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    username = ''

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password',)

class EmployerForm(forms.ModelForm):

    profile_img = forms.ImageField(required=False)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER), required=True)
    dob = forms.DateField(widget=forms.DateInput())
    contact_no = forms.CharField(max_length=10, required=True)
    captcha = CaptchaField()
    tc = forms.BooleanField(widget=forms.CheckboxInput(), required=True)
    admin_approval = False

    class Meta:
        model = Employer
        fields = ('state','city','profile_img', 'gender', 'dob', 'contact_no', 'captcha', 'tc',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        exclude = ('employer','logo',)

class JobSeekerForm(forms.ModelForm):      
    profile_img = forms.ImageField(required=False)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER), required=True)
    dob = forms.DateField(widget=forms.DateInput())
    contact_no = forms.CharField(max_length=10, required=True)
    captcha = CaptchaField()
    tc = forms.BooleanField(widget=forms.CheckboxInput(), required=True)

    class Meta:
        model = JobSeekers
        fields = ('state','city','profile_img', 'gender', 'dob', 'contact_no', 'captcha', 'tc',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')

#------
#karishma's form
class JobForm(forms.ModelForm):
    class Meta:
       model = AddJob
       exclude = ('posted_date','employer','slug',)


class EditJobForm(forms.ModelForm):
    class Meta:
       model = AddJob
       exclude = ('posted_date','employer','slug',)

class ResumeForm(forms.ModelForm):
    preffered_job_location = forms.CharField(required=True)
    class Meta:
        model = Resume
        fields = ('resumetitle','preffered_job_location','state','city','category','subcategory','totalexp','currentsalary',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')