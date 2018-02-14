from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from jportal.models import Category, SubCategory
from jportal.models import Education, AddJob
from jportal.models import Employer, EmployerCompanyProfile
from jportal.models import JobSeekers, State, City, JobSeekersProfile
from jportal.models import Graduation, Post_Graduation, PhD

from jportal.forms import EmployerForm, JobSeekerForm, UserForm, AddJobForm, EmployerCompanyProfileForm, EditJobForm
from jportal.forms import UserEditForm, EmployerEditForm, GraduationForm,PostGraduationForm,PhDForm
from jportal.forms import ClassXIIForm,ClassXForm 
from django.utils import timezone

from datetime import datetime

def user_type(ek_req):
    usertype=''
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

def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'jportal/city_dropdown_list_options.html', {'cities': cities})

def index(request):
    print(request.user)

    usertype = user_type(request)

    return render(request, 'jportal/index.html', {'usertype':usertype})

def about(request):
    
    usertype = user_type(request)
    return render(request, 'jportal/about', {'usertype':usertype})

#---------------------EMPLOYER----------------------
def employer_reg(request):
    
    user_form = UserForm()
    employer_form = EmployerForm()
    
    print(request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employer_form = EmployerForm(request.POST,request.FILES)
        
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
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/jportal/')

        else:
            print(employer_form.errors)
            print(user_form.errors)
    
    context_dict = {'employer_form':employer_form, 'user_form':user_form, }

    return render(request, 'registration/employer_register.html', context_dict)

def employer_profile(request,username):
    context_dict = {}
    print(request.user)
    usertype = user_type(request)
    if request.method == 'GET':
        emp_usr = User.objects.get(username=username)
        print(emp_usr.username)

        emp_data = Employer.objects.get(user_id=emp_usr.id)
        try:
            company_data = EmployerCompanyProfile.objects.get(employer_id=emp_data.id)
        except EmployerCompanyProfile.DoesNotExist:
            company_data = ''
            company_form = EmployerCompanyProfileForm()
            context_dict['company_form'] = company_form
    if request.method == 'POST':
        emp_usr = User.objects.get(username=username)
        print(emp_usr.username)
        emp_data = Employer.objects.get(user_id=emp_usr.id)
        company_form = EmployerCompanyProfileForm(request.POST,request.FILES)
        if company_form.is_valid():
            company_data= company_form.save(commit=False) 
            company_data.employer = emp_data
            company_data.save()
            return redirect('employer_profile',username=emp_usr.username)
        else:
            print(company_data.errors)
        context_dict['company_form'] = company_form
    context_dict['emp_usr'] = emp_usr
    context_dict['emp_data'] = emp_data
    context_dict['usertype'] = usertype
    context_dict['company_data'] = company_data
    return render(request, 'jportal/employer_profile.html', context_dict)

def edit_employer_profile(request, username):
    usertype = user_type(request)
    user = User.objects.get(username=username)
    emp = Employer.objects.get(user_id=user.id)
    if request.method == "POST":
        user_form = UserEditForm(request.POST, request.FILES, instance=user)
        emp_form = EmployerEditForm(request.POST, request.FILES, instance=emp)
        if user_form.is_valid() and emp_form.is_valid():
            user_edit = user_form.save(commit=False)
            user_edit.username = user_edit.email
            user_edit.save()
            emp_form.save(commit=True)
            return redirect('employer_profile',username=user_edit.username)
    else:
        user_form = UserEditForm(instance=user)
        emp_form = EmployerEditForm(instance=emp)
    context_dict={'user_form':user_form, 'emp_form':emp_form,'usertype':usertype}     
    return render(request, 'jportal/emp_edit.html', context_dict)

def edit_company_details(request):
    context_dict = {}
    usertype = user_type(request)
    emp = Employer.objects.get(user_id=request.user.id)
    company = EmployerCompanyProfile.objects.get(employer_id=emp.id)
    if request.method == "POST":
        company_form = EmployerCompanyProfileForm(request.POST,request.FILES, instance=company)
        if company_form.is_valid():
            company_form.save()
        return redirect('employer_profile',username=request.user.username)
    else:
       company_form = EmployerCompanyProfileForm(instance=company)
    context_dict = {'company_form':company_form, 'usertype':usertype}
    return render(request, 'jportal/company_edit.html', context_dict)

#--------------------JOB SEEKER--------------------------
def jobseeker_reg(request):

    user_form = UserForm()
    job_seek = JobSeekerForm()

    print(request)
    if request.method == 'POST' :
        user_form = UserForm(request.POST)
        job_seek = JobSeekerForm(request.POST,request.FILES)
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
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/jportal/')

        else:
            print(user_form.errors)
            print(job_seek.errors)
 
    context_dict = {'job_seek':job_seek, 'user_form':user_form, }

    return render(request, 'registration/jobseeker_register.html', context_dict)

def jobseeker_profile(request,username):
    context_dict = {}
    print(request.user)
    usertype = user_type(request)
    if request.method == 'GET':
        user = User.objects.get(username=username)
        print(user.username)
        seeker = JobSeekers.objects.get(user_id=user.id)
        context_dict['user'] = user
        context_dict['seeker'] = seeker
        context_dict['usertype'] = usertype 
    return render(request, 'jportal/jobseeker_profile.html', context_dict)


#-------------------------Job--------------------
def add_job(request):
    print(request.user)
    usertype = user_type(request)
    emp = Employer.objects.get(user_id=request.user.id)
    form=AddJobForm()
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            job = form.save(commit=False) 
            job.employer = emp
            job.posted_date = timezone.now()
            job.save()

            return index(request)
        else:
            print(form.errors)
    return render(request, 'jportal/add_job.html', {'form': form,'usertype':usertype,})
    
def manage_job(request):
    print(request.user)
    try:
        
        emp = Employer.objects.get(user_id=request.user.id)
        jobs = AddJob.objects.filter(employer_id=emp.id)
        print(jobs)
    except AddJob.DoesNotExist:
        print("Kassu nathi")
        return redirect('index.html')

    usertype = user_type(request)        
    context_dict={'job': jobs,'usertype':usertype,}
    return render(request, 'jportal/managejob.html', context_dict) 

def edit_job(request,addjob_title_slug):
    try:
        b = AddJob.objects.get(slug=addjob_title_slug)
    except AddJob.DoesNotExist:
        return redirect('add_job.html')
    
    b = AddJob.objects.get(slug=addjob_title_slug)
    print(b)
    form = EditJobForm({'category':b.category, 'subcategory':b.subcategory, 'title':b.title,'last_date':b.last_date,'Job_responsibility':b.Job_responsibility,'candidate_profile':b.candidate_profile})
    print(form)
    if request.method == 'POST':
        form = EditJobForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            if a.category:
                b.category = a.category
            if a.subcategory:
                b.subcategory = a.subcategory
            if a.last_date:
                b.last_date = a.last_date
            if a.salary:
                b.salary = a.salary
            if a.title:
                b.title = a.title
            if a.Job_responsibility:
                b.Job_responsibility = a.Job_responsibility            
            if a.candidate_profile:
                b.candidate_profile = a.candidate_profile
  
            b.save()
            return redirect('/jportal/managejob/')
            
        else:
            print(form.errors)
    usertype = user_type(request)
    return render(request, 'jportal/edit_job.html', {'form':form,'usertype':usertype,})

def delete_job(request,addjob_title_slug):
    try:
        a = AddJob.objects.get(slug=addjob_title_slug)
    except AddJob.DoesNotExist:
        return redirect('index.html')
    
    if a:
        AddJob.objects.get(slug=addjob_title_slug).delete()
    
    return redirect('managejob')


#testing remaining..
def show_appliers(request):
    usertype = user_type(request)
    context_dict={}
    if request.method == 'GET':
        job_id = request.GET['job_id']
        appliers = Appliers.objects.filter(job_id=job_id)
        context_dict['appliers'] = appliers
        context_dict['usertype'] = usertype
        return render(request, 'jportal/appliers.html', context_dict)

#testing remaining..
def show_jobs_applied(request):
    usertype = user_type(request)
    if request.method == 'GET':
        jobseeker_id = request.GET['jobseeker_id']
        job_ids= Appliers.objects.values_list('job_id',flat=True).filter(appliers_id=jobseeker_id)
        jobs_applied = Job.objects.filter(pk__in=set(job_ids))
        return render(request, 'jportal/jobs_applied.html', {'jobs_applied':jobs_applied,'usertype':usertype,})

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
    usertype = user_type(request)
    emp_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
        emp_list = get_employer_list(8, starts_with)
    return render(request, 'jportal/.html', {'emps': emp_list,'usertype' : usertype})

def get_job_list(max_results=0, starts_with=''): 
    job_list = []
    if starts_with:
        job_list = Job.objects.filter(name__istartswith=starts_with)
    if max_results > 0:
        if len(job_list) > max_results:
            job_list = job_list[:max_results] 
    return job_list

def suggest_job(request): 
    usertype = user_type(request)
    job_list = []
    starts_with = ''
    if request.method == 'POST':
        starts_with = request.POST['suggestion']   
        job_list = get_job_list(8, starts_with)
    return render(request, 'jportal/.html', {'jobs': job_list,'usertype':usertype})

def add_education(request,username):
    usertype=user_type(request)
    user=User.objects.get(username=username)
    job_seek=JobSeekers.objects.get(user_id=user.id)
    seek_profile=JobSeekersProfile(user_id=job_seek.id)
    g_form = GraduationForm()
    pg_form = PostGraduationForm()
    phd_form = PhDForm()
    context_dict={'g_form':g_form,'pg_form':pg_form,'phd_form':phd_form}
    if request.method  == 'POST':
        if 'add_graduation' in request.POST:
            g_form=GraduationForm(request.POST)
            pg_form = PostGraduationForm()
            phd_form = PhDForm()
            if g_form.is_valid():
                g_detail=g_form.save(commit=False)
                g_detail.category = 'graduation'
                print(g_detail.category)
                g_detail.save()
                context_dict={'g_form':g_detail,'pg_form':pg_form,'phd_form':phd_form}
            else:
                print(g_form.errors)
        if 'add_post_graduation' in request.POST:
            pg_form=PostGraduationForm(request.POST)
            g_form = GraduationForm()
            phd_form = PhDForm()
            if pg_form.is_valid():
                pg_detail=pg_form.save(commit=False)
                pg_detail.category = 'post_graduation'
                print(pg_detail.category)
                pg_detail.save() 
                context_dict={'pg_form':pg_detail,'g_form':g_form,'phd_form':phd_form}
            else:
                print(g_form.errors)
        if 'add_phd' in request.POST:
            phd_form=PhDForm(request.POST)
            g_form = GraduationForm()
            pg_form = PostGraduationForm()
            if phd_form.is_valid():
                phd_detail=phd_form.save(commit=False)
                phd_detail.category = 'phd'
                print(phd_detail.category)
                phd_detail.save()
                context_dict={'phd_form':phd_detail,'g_form':g_form,'pg_form':pg_form,}
            else:
                print(g_form.errors)
    return render(request,'jportal/education.html',context_dict)



    