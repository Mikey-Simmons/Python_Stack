from django.shortcuts import render, HttpResponse, redirect
from .models import User
def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request,'index.html',context)
def submit(request):

    User.objects.create(
        first_name = request.POST['firstname'],
        last_name =request.POST['lastname'],
        email= request.POST['email'],
        age= request.POST['age'])
    return redirect('/')