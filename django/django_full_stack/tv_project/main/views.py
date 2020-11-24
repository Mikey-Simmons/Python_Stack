from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import TVShow

def index(request):
    context ={
        "all_shows": TVShow.objects.all()
    }
    return render(request,'shows.html',context)
def new_show_page(request):
    return render(request,'new_show.html')

def add_show(request):
    errors = TVShow.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k,v in errors.items():
            messages.error(request,v)
        return redirect('/shows/new')
    else:
        TVShow.objects.create(
        title = request.POST['title'],
        release_date = request.POST['release_date'],
        desc = request.POST['description'],
        network = request.POST['network']
        )   
        messages.success(request, "tv show added...")
    return redirect('/shows')

def show_display(request,num):
   
    context = {
        "show_to_display": TVShow.objects.get(id = num)
    }
    return render(request,'show_details.html',context)
def edit_show_page(request,num):
    context = {
        "show_to_edit": TVShow.objects.get(id=num)
    }
    return render(request,'edit_show.html',context)
def edit_show(request):
    show_to_edit = TVShow.objects.get(id = request.POST['show_id'])
    show_to_edit.title = request.POST['title']
    show_to_edit.release_date = request.POST['release_date']
    show_to_edit.desc = request.POST['description']
    show_to_edit.network = request.POST['network']
    num = show_to_edit.id
    show_to_edit.save()
    return redirect(f'/shows/{num}')