from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from jportal.models import Category, SubCategory
from jportal.models import Education, Job , AddJob
from jportal.models import Employer, EmployerProfile
from jportal.models import JobSeekers, JobSeekersProfile

from jportal.forms import EmployerForm, JobSeekerForm, UserForm, JobForm
from jportal.forms import EmployerProfileForm

from datetime import datetime

#index for testing purpose...
def index(request):
    print(request.user)

    context_dict = {}
    #checking the type of user. i.e Employer or JobSeeker
    #Lame Logic -_-
    if request.user:
        u = request.user.id
        print(u)
        try:
            e=Employer()
            e = Employer.objects.get(user_id=u) 
            if e:
                print("Employer")

                return render(request, 'jportal/employer_page.html', context_dict)

        except e.DoesNotExist:
            pass

        try:
            e=JobSeekers()
            e = JobSeekers.objects.get(user_id=u) 
            if e:
                print("JobSeeker")
                #ahiya job seeker page aavse
        except e.DoesNotExist:
            pass        

    return render(request, 'jportal/index.html', {'content':'YO'})

def about(request):
    return HttpResponse("About Page")

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
    if request.method == 'POST':
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
    print(request)
    usid = request.user.id
    try:
        user = Employer.objects.get(user_id=usid)
    except Employer.DoesNotExist:
        return redirect('/employer_page/')

    emp = EmployerProfile.objects.get_or_create(employer=user)[0]
    e_profile = EmployerProfileForm({'company_name':emp.company_name, 'description':emp.description, 'address':emp.address })
    
    if request.method == 'POST':
        e_profile = EmployerProfileForm(request.POST, request.FILES)
        if e_profile.is_valid():
            emp_prof = e_profile.save(commit=False)
            emp_prof.employer_id = emp.employer_id
            emp_prof.save()

            return redirect('/jportal/employer_profile/')
        else:
            print(e_profile.errors)

    context_dict['e_profile'] = e_profile
    context_dict['user'] = user
    context_dict['emp_profile'] = emp

    return render(request, 'jportal/employer_profile.html', context_dict)

#Employer dashboard implementation
def employer_page(request):
    
    print(request)

    return render(request, 'jportal/employer_page.html', {'user': request.user })

def detail_employer(request):
    print(request)    
    context_dict = {}

    print(request.user.id)
    #print(request.user.email)
    if request.method == 'GET':
        emp_usr = User.objects.get(id=request.user.id)
        print(emp_usr.username)

        emp_data = Employer.objects.get(user_id=emp_usr.id)
        
        context_dict['emp_usr'] = emp_usr
        context_dict['emp_data'] = emp_data

    return render(request, 'jportal/detail_employer.html', context_dict)

#testing remaining..
def job_listing(request):

    try:
        category = Category.objects.get()
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

#----karishma's Okay Up and running
def add_job(request):
    print(request.user)

    emp = Employer.objects.get(user_id=request.user.id)
    form=JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            a = form.save(commit=False) 
            a.employer = emp
            a.posted_date = datetime.now()
            a.save()

            return index(request)
        else:
            print(form.errors)
    return render(request, 'jportal/add_job.html', {'form': form})

def manage_job(request):
    print(request.user)
    try:
        emp = Employer.objects.get(user_id=request.user.id)
        jobs = AddJob.objects.filter(employer_id=emp.id)
        print(jobs)
    except AddJob.DoesNotExist:
        print("Kassu nathi")
        return redirect('index.html')
        
    context_dict={'job_title': jobs}
    return render(request, 'jportal/managejob.html', context_dict) 

def edit_job(request,addjob_title_slug):
    context_dict = {}
    try:
        j_title = AddJob.objects.get(slug=addjob_title_slug)
    except AddJob.DoesNotExist:
        return redirect('add_job.html')
    
    ejob = AddJob.objects.get(slug=addjob_title_slug)
    print(ejob)
    e_job = JobForm({'category':ejob.category, 'subcategory':ejob.subcategory, 'title':ejob.title,'last_date':ejob.last_date,'Job_responsibility':ejob.Job_responsibility,'candidate_profile':ejob.candidate_profile})
    
    if request.method == 'POST':
        e_job = JobForm(request.POST)
        if e_job.is_valid():
            adde_job = e_job.save(commit=False)
            e_job = adde_job
            e_job.save()

            return redirect('/jportal/managejob/')
        else:
            print(e_job.errors)

    context_dict['e_job'] = e_job
    return render(request, 'jportal/edit_job.html', context_dict)





