from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'counter' in request.session:
        request.session['counter'] +=1
    return render(request,"index.html")

def destroy(request):
    if 'counter' in request.session:
        request.session['counter'] =0
    return redirect("/")

