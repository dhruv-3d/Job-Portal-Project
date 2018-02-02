from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from jportal.models import Category, SubCategory
from jportal.models import Education, Job, AddJob
from jportal.models import Employer, EmployerCompanyProfile
from jportal.models import JobSeekers, JobSeekersProfile
from jportal.models import Job

from jportal.forms import EmployerForm, JobSeekerForm, UserForm, AddJobForm
from jportal.forms import EmployerCompanyProfileForm

from datetime import datetime

def user_type(ek_req):
    usertype=''
    context_dict = {}
    #checking the type of user. i.e Employer or JobSeeker
    #Lame Logic -_-
    if ek_req.user:
        u = ek_req.user.id
        print(u)
        try:
            e=Employer()
            e = Employer.objects.get(user_id=u) 
            if e:
                usertype='e'
                print("Employer: ",usertype)
        except e.DoesNotExist:
            pass

        try:
            e=JobSeekers()
            e = JobSeekers.objects.get(user_id=u) 
            if e:
                usertype='j'
                print("JobSeeker: ",usertype)
        except e.DoesNotExist:
            pass

    return usertype


#index for testing purpose...
def index(request):
    print(request.user)

    usertype = user_type(request)

    return render(request, 'jportal/index.html', {'usertype':usertype})

def about(request):
    
    usertype = user_type(request)
    return render(request, 'jportal/about', {'usertype':usertype})

#---------------------EMPLOYER REGISTRATION
def employer_reg(request):
    
    user_form = UserForm()
    employer_form = EmployerForm()
    
    print(request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employer_form = EmployerForm(request.POST)
        
        if employer_form.is_valid() and user_form.is_valid():    
            user = user_form.save(commit=False)
            user.username = user.email
            user.password = user_form.cleaned_data.get('password')
            user.password = make_password(user.password)
            print(user.password)
            user.save()
            usr_obj = User.objects.get(username=user.username)
            print("aa user obj:",usr_obj)

            emp_user = employer_form.save(commit=False)
            emp_user.user = usr_obj

            emp_user.save()

            return redirect('/jportal/')

        else:
            print(employer_form.errors)
            print(user_form.errors)
    
    context_dict = {'employer_form':employer_form, 'user_form':user_form, }

    return render(request, 'registration/employer_register.html', context_dict)


#--------------------JOB SEEKER REGISTRATION
def jobseeker_reg(request):

    user_form = UserForm()
    job_seek = JobSeekerForm()

    print(request)
    if request.method == 'POST' :
        user_form = UserForm(request.POST)
        job_seek = JobSeekerForm(request.POST)
        if user_form.is_valid() and job_seek.is_valid():
            user = user_form.save(commit=False)
            user.username = user.email
            user.password = user_form.cleaned_data.get('password')
            user.password = make_password(user.password)
            print(user.password)
            user.save()
            usr_obj = User.objects.get(username=user.username)
            print("aa user obj:",usr_obj)
            
            seeker_user = job_seek.save(commit=False)
            seeker_user.user = usr_obj
            seeker_user.save()

            return redirect('/jportal/')

        else:
            print(user_form.errors)
            print(job_seek.errors)
 
    context_dict = {'job_seek':job_seek, 'user_form':user_form, }

    return render(request, 'registration/jobseeker_register.html', context_dict)

def employer_profile(request):
    context_dict = {}
    print(request.user)
    usertype = user_type(request)
    if request.method == 'GET':
        emp_usr = User.objects.get(id=request.user.id)
        print(emp_usr.username)

        emp_data = Employer.objects.get(user_id=emp_usr.id)
        company_data = EmployerCompanyProfile.objects.get(emp_id=emp_data.id)
        context_dict['emp_usr'] = emp_usr
        context_dict['emp_data'] = emp_data
        context_dict['company_data'] = company_data
        context_dict['usertype'] = usertype
    return render(request, 'jportal/employer_profile.html', context_dict)

def company_profile(request, username):
    context_dict = {}
    print(request.user)

    try:
        user = User.objects.get(username=username)
        euser = Employer.objects.get(user_id=user.id)
    except Employer.DoesNotExist:
        print('No such employer')

    #-----Retriving data of EmployerProfile
    emp = EmployerCompanyProfileForm.objects.get_or_create(employer_id=euser.id)[0]
    e_profile = EmployerCompanyProfileForm({'company_name':emp.company_name, 'description':emp.description, 'address':emp.address })

    if request.method == 'POST':
        e_profile = EmployerCompanyProfileForm(request.POST)
        if e_profile.is_valid():

            #EmployerProfile ma update thai che ahiya--------
            emp_prof = e_profile.save(commit=False)
            emp.company_name = emp_prof.company_name
            emp.description = emp_prof.description
            emp.address = emp_prof.address
            emp.save()
            return redirect('employer_profile', user.username)
        else:
            print(e_profile.errors)

    context_dict['e_profile'] = e_profile
    context_dict['selected_user'] = user
    context_dict['emp_profile'] = emp

    return render(request, 'jportal/edit_emp_prof.html', context_dict)

#----karishma's
def add_job(request):
    print(request.user)
    emp = Employer.objects.get(user_id=request.user.id)
    form=JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            job = form.save(commit=False) 
            job.employer = emp
            job.posted_date = datetime.now()
            job.save()

            return index(request)
        else:
            print(form.errors)
    return render(request, 'jportal/add_job.html', {'form': form})
    
def manage_job(request):
    return render(request, 'jportal/managejob.html')

#testing remaining..
def job_listing(request):
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
    return render(request, 'jportal/job.html', context_dict)

#vidushi's
#testing remaining..
def show_appliers(request):
    context_dict={}
    if request.method == 'GET':
        job_id = request.GET['job_id']
        appliers = Appliers.objects.filter(job_id=job_id)
        context_dict['appliers']=appliers
        return render(request, 'jportal/appliers.html', context_dict)

#testing remaining..
def show_jobs_applied(request):
    if request.method == 'GET':
        jobseeker_id = request.GET['jobseeker_id']
        job_ids= Appliers.objects.values_list('job_id',flat=True).filter(appliers_id=jobseeker_id)
        jobs_applied = Job.objects.filter(pk__in=set(job_ids))
        return render(request, 'jportal/jobs_applied.html', {'jobs_applied':jobs_applied})

#testing remaining..
def get_employer_list(max_results=0, starts_with=''): 
    emp_list = []
    if starts_with:
        emp_list = Employer.objects.filter(name__istartswith=starts_with)
    if max_results > 0:
        if len(emp_list) > max_results:
            emp_list = emp_list[:max_results] 
    return emp_list

def suggest_employer(request): 
    emp_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
        emp_list = get_employer_list(8, starts_with)
    return render(request, 'jportal/.html', {'emps': emp_list })

def get_job_list(max_results=0, starts_with=''): 
    job_list = []
    if starts_with:
        job_list = Job.objects.filter(name__istartswith=starts_with)
    if max_results > 0:
        if len(job_list) > max_results:
            job_list = job_list[:max_results] 
    return job_list

def suggest_job(request): 
    job_list = []
    starts_with = ''
    if request.method == 'POST':
        starts_with = request.POST['suggestion']   
        job_list = get_job_list(8, starts_with)
    return render(request, 'jportal/.html', {'jobs': job_list })

def employer_profile(request): 
    context_dict={}
    if request.method == 'GET':
        emp_usr = User.objects.get(id=request.user.id)
        print(emp_usr.username)
        emp_data = Employer.objects.get(user_id=emp_usr.id)
        
        context_dict['emp_usr'] = emp_usr
        context_dict['emp_data'] = emp_data

    return render(request, 'jportal/employer_profile.html', context_dict)
