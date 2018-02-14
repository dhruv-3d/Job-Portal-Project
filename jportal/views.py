from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from jportal.models import Category, SubCategory
from jportal.models import Education, Depend, AddJob
from jportal.models import Employer, EmployerCompanyProfile
from jportal.models import JobSeekers, JobSeekersProfile
from jportal.models import Depend, Appliers

from jportal.forms import EmployerForm, JobSeekerForm, UserForm, JobForm
from jportal.forms import EmployerCompanyProfileForm, Resume
from jportal.forms import SearchForm, UserEditForm, EmployerEditForm

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

#index for testing purpose...!!!
def index(request):
    print(request.user)

    context_dict = {}
    context_dict['user_type'] = user_type(request)

    context_dict['searchform'] = SearchForm()
    context_dict['jobs'] = job_listing(request)

    return render(request, 'jportal/index.html', context_dict)

def about(request):
    return HttpResponse("About Page")

#---------------------EMPLOYER REGISTRATION
def employer_reg(request):
    context_dict = {}

    user_form = UserForm()
    employer_form = EmployerForm()
    
    print(request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employer_form = EmployerForm(request.POST, request.FILES)
        
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
            login(request)
            return index(request)

        else:
            print(employer_form.errors)
            print(user_form.errors)
    
    context_dict['employer_form'] = employer_form 
    context_dict['user_form'] = user_form
    
    return render(request, 'registration/employer_register.html', context_dict)

#--------------------JOB SEEKER REGISTRATION
def jobseeker_reg(request):
    context_dict = {}
    user_form = UserForm()
    job_seek = JobSeekerForm()

    print(request)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        job_seek = JobSeekerForm(request.POST, request.FILES)
        if user_form.is_valid() and job_seek.is_valid():
            user = user_form.save(commit=False)
            seeker_user = job_seek.save(commit=False)

            user.username = user.email
            user.password = user_form.cleaned_data.get('password')
            user.password = make_password(user.password)
            
            user.save()
            usr_obj = User.objects.get(username=user.username)
            print("aa user obj:",usr_obj)
            
            seeker_user.user_id = usr_obj.id
            seeker_user.save()
            login(request, user)
            redirect('index')

        else:
            print(user_form.errors)
            print(job_seek.errors)
 
    context_dict['job_seek'] = job_seek 
    context_dict['user_form'] = user_form

    return render(request, 'registration/jobseeker_register.html', context_dict)

#------------Job seeker (by karishma)
def jobseeker_edit(request):
    context_dict = {}
    form = JobSeekerForm()
    try:
        b = JobSeekers.objects.get(user_id=request.user.id)   
    except JobSeekers.DoesNotExist():
        b = None
    print(b.state)
    
    if b:
        print('pass')
        form = JobSeekerForm({'state':b.state,'city':b.city,'profile_img':b.profile_img,'gender':b.gender,'dob':b.dob,'contact_no':b.con_no})
        if request.method == 'POST':
            form = JobSeekerForm(request.POST, request.FILES)
            if form.is_valid():
                print('valid che')
                c = form.save(commit=False)                
                b.user_id = request.user.id
                b = c
                b.save()
                return redirect('index')
                
            else:
                print(form.errors)

    context_dict['user_type'] = user_type(request)
    context_dict['form'] = form
    return render(request, 'jportal/jobseeker_edit.html', context_dict)

def register(request):
    context_dict = {}
    
    return render(request, 'registration/register.html', context_dict)

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
        company_form = EmployerCompanyProfileForm(request.POST)

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
        user_form = UserEditForm(request.POST, instance=user)
        emp_form = EmployerEditForm(request.POST, instance=emp)

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
        company_form = EmployerCompanyProfileForm(request.POST, instance=company)

        if company_form.is_valid():
            company_form.save()
        
            return redirect('employer_profile',username=request.user.username)
    else:
       company_form = EmployerCompanyProfileForm(instance=company)

    context_dict = {'company_form':company_form, 'usertype':usertype}

    return render(request, 'jportal/company_edit.html', context_dict)

#Employer dashboard implementation
def employer_page(request):
    print(request)
    context_dict = {}

    context_dict['user_type'] = user_type(request)
    return render(request, 'jportal/employer_page.html', context_dict)

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

def jobseeker_page(request):
    print(request)

    return render(request, 'jportal/jobseeker_page.html', {'user': request.user })

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

            return redirect('managejob')
        else:
            print(form.errors)
    return render(request, 'jportal/add_job.html', {'form': form})

def resume(request):
    user = request.user.id
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False) 
            a.jobseeker_id = user
            a.save()
            return redirect('index')
        else:
            print(form.errors)
    return render(request, 'jportal/resume.html', {'form': form})

#----vidushi's------------------------
#----overwritten and was converted into job search function---
def job_listing(request):
    print(request)
    context_dict = {}
    usertype = None
    usertype = user_type(request)

    #will execute when view is called from managejob view for employer
    if request.method == 'GET' and usertype == 'e':
        try:
            emp = Employer.objects.get(user_id=request.user.id)
            jobs = AddJob.objects.filter(employer_id=emp.id)
            return jobs
        except AddJob.DoesNotExist:
            return HttpResponse("No Jobs Posted")
    
    elif request.method == 'GET'  and "jobtitle" in request.GET: 

        try:
            cat_title = request.GET['category']
            subcat_name = request.GET['subcategory']
            #print("aa job mailu :",job_title)

            if cat_title:   #getting job as per category
                cat = Category.objects.get(id=cat_title)

                if subcat_name:     #getting job as per subcategory
                    subcat = SubCategory.objects.get(id=subcat_name)
                    
                    jobs = AddJob.objects.filter(subcategory_id=subcat.id)
                    return jobs
                
                jobs = AddJob.objects.filter(category_id=cat.id)            
                return jobs

        except AddJob.DoesNotExist:
            print("Category wala thi ni mailu job")

        try:
            job_title = request.GET.get('jobtitle')
            print("ehehehehe")
            if job_title:
                job_srch = job_title.split()
                jobs = AddJob.objects.filter(slug__icontains=job_srch[0])
                return jobs
        except:
            print("Title thi pan ni mailu job")


    return ''  #none found

#-----------apply for job
def job_details(request, jobslug_name):
    context_dict = {}
    usertype = None
    usertype = user_type(request)
    context_dict['user_type'] = usertype

    if request.method == "GET":

        #getting job information
        job_info = AddJob.objects.get(slug=jobslug_name)
        print(job_info)

        #checking jobseeker has applied or not
        if usertype == 'j':
            seeker = JobSeekers.objects.get(user_id=request.user.id)
            print(seeker)
            try:
                applier = Appliers.objects.get(jobseeker_id=seeker.id, job_id=job_info.id)
                context_dict['seeker'] = seeker
                context_dict['applier'] = applier
            except Appliers.DoesNotExist:
                context_dict['seeker'] = seeker

        elif usertype == 'e':
            employer = Employer.objects.get(user_id=request.user.id)
            try:
                postedjob = AddJob.objects.get(employer_id=employer.id)
                context_dict['employer'] = employer
                context_dict['postedjob'] = postedjob
            except AddJob.DoesNotExist:
                context_dict['employer'] = employer
        
    context_dict['job_info'] = job_info
    return render(request, 'jportal/job_details.html', context_dict)

#--------
@login_required
def jobs_applied(request):
    print(request)

    context_dict = {}
    if request.method == 'GET':
        seeker = JobSeekers.objects.get(user_id=request.user.id)
        applied = Appliers.objects.filter(jobseeker_id=seeker.id)
        all_jobs  =AddJob.objects.all()

        context_dict['applied_jobs'] = applied
        context_dict['all_jobs'] = all_jobs

    return render(request, 'jportal/jobs_applied.html', context_dict)

@login_required
def job_apply(request, jobslug_name):
    context_dict = {}

    if request.method == "GET":
        seeker = JobSeekers.objects.get(user_id=request.user.id)
        job = AddJob.objects.get(slug=jobslug_name)
        applier = None
        try:
            applier = Appliers.objects.get(job_id=job.id, jobseeker_id=seeker.id)
        except:
            pass

        if applier:
            context_dict['applied_before'] = applier
        else:
            applier = Appliers()
            applier.date_apply = datetime.now()
            applier.status = 'pending'
            applier.job_id = job.id
            applier.jobseeker_id = seeker.id
            applier.save()

            return job_apply(request, jobslug_name)

        context_dict['applier'] = applier
    
    return render(request, 'jportal/job_apply.html', context_dict)

#----vidushi's view..but overwritten------------------------
#-------------Done
def job_applications(request):
    context_dict={}

    if request.method == 'GET':
        
        employer = Employer.objects.get(user_id=request.user.id)
        jobs = AddJob.objects.filter(employer_id=employer.id)

        context_dict['employer'] = employer
        context_dict['jobs'] = jobs

        return render(request, 'jportal/job_applications.html', context_dict)

#-----baaki
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


def suggest_job(request): 
    job_list = []
    starts_with = ''
    if request.method == 'POST':
        starts_with = request.POST['suggestion']   
        job_list = get_job_list(8, starts_with)
    return render(request, 'jportal/.html', {'jobs': job_list })

#--------------------------------------
def manage_job(request):
    print(request.user)
    context_dict = {}

    if request.method == 'GET':
        context_dict['user_type'] = user_type(request)
        context_dict['jobs'] = job_listing(request)

    return render(request, 'jportal/managejob.html', context_dict) 

def edit_job(request,addjob_title_slug):
    try:
        b = AddJob.objects.get(slug=addjob_title_slug)
    except AddJob.DoesNotExist:
        return redirect('add_job.html')
    
    b = AddJob.objects.get(slug=addjob_title_slug)
    print(b)
    form = JobForm({'category':b.category, 'subcategory':b.subcategory, 'title':b.title,'last_date':b.last_date,'Job_responsibility':b.Job_responsibility,'candidate_profile':b.candidate_profile})
    print(form)
    if request.method == 'POST':
        form = JobForm(request.POST)
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

    return render(request, 'jportal/edit_job.html', {'form':form})

def delete_job(request,addjob_title_slug):
    try:
        a = AddJob.objects.get(slug=addjob_title_slug)
    except AddJob.DoesNotExist:
        return redirect('index.html')
    
    if a:
        AddJob.objects.get(slug=addjob_title_slug).delete()
    
    return redirect('managejob')