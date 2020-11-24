from django.shortcuts import render, HttpResponse, redirect
from .models import User, Job
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'index.html')
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        password=request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = pw_hash
    )
    messages.success(request,"User Successfully created!")
    request.session['user_id'] = new_user.id
    return redirect('/welcome')
def welcome(request):
    if 'user_id' in request.session:
        logged_in_user = User.objects.get(id=request.session['user_id'])
        all_jobs = Job.objects.all()
        context = {
        'logged_in_user': logged_in_user,
        'all_jobs' : all_jobs
        }
        return render(request,'welcome.html',context)
    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/') 
    list_of_users = User.objects.filter(email=request.POST['email'])
    if len(list_of_users) > 0:
        user = list_of_users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/welcome')

    return redirect('/')
def newjob(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    all_jobs = Job.objects.all()
    context = {
        'logged_in_user': logged_in_user,
        'all_jobs' : all_jobs
    }
    return render(request,'new_job.html',context)

def addjob(request):
    errors = Job.objects.job_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/new')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    all_jobs = Job.objects.all()
    new_job = Job.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
        location = request.POST['location'],
        uploaded_by = logged_in_user
    )
    context = {
        'logged_in_user': logged_in_user,
        'all_jobs' : all_jobs
    }
    return redirect('/welcome')
def displayjob(request,num):
    job_to_display = Job.objects.get(id = num)
    logged_in_user = User.objects.get(id=request.session['user_id'])
    context = {
        "job_to_display" : job_to_display,
        "logged_in_user" : logged_in_user,
    }
    return render(request,'job_display.html',context)
def addjob_to_user(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    job_to_add = Job.objects.get(id=request.POST['job_id'])
    logged_in_user.users_jobs.add(job_to_add)
    return redirect('/welcome')
def job_edit_page(request,num):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    job_to_edit = Job.objects.get(id=request.POST['job_id'])
    num = job_to_edit.id
    context = {
        'job_to_edit' : job_to_edit,
        'logged_in_user': logged_in_user,
        'num' : num
    }
    return render(request,'edit_job.html',context)
def editjob(request,num):
    errors = Job.objects.job_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/new')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    job_to_edit = Job.objects.get(id=num)
    num = job_to_edit.id
    job_to_edit.title = request.POST['title']
    job_to_edit.desc = request.POST['desc']
    job_to_edit.location = request.POST['location']
    job_to_edit.save()
    context = {
        'job_to_edit' : job_to_edit,
        'logged_in_user': logged_in_user,
        'num' : num
    }
    return redirect(f"/jobs/{num}")
def delete_job(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    job_to_delete = Job.objects.get(id=request.POST['job_id'])
    job_to_delete.delete()
    return redirect('/welcome')