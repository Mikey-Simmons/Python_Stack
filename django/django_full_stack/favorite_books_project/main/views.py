from django.shortcuts import render, HttpResponse, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt
# Create your views here.
from django.shortcuts import render, HttpResponse
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
    return redirect('/books')
def books(request):
    if 'user_id' in request.session:
        logged_in_user = User.objects.get(id=request.session['user_id'])
        all_books = Book.objects.all()
        context = {
        'logged_in_user': logged_in_user,
        'all_books' : all_books
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
            messages.success(request,"Login Successful")
            return redirect('/books')

    return redirect('/')
def addbook(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/books')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    all_books = Book.objects.all()
    new_book = Book.objects.create(
    title = request.POST['title'],
    desc = request.POST['desc'],
    uploaded_by = logged_in_user
    )
    logged_in_user.liked_books.add(new_book)
    context = {
        'logged_in_user': logged_in_user,
        'all_books' : all_books
        }
    return redirect('/books')
def addfav(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    fav_book = Book.objects.get(id =request.POST['book_id'])
    logged_in_user.liked_books.add(fav_book)
    return redirect('/books')
def displaybook(request,num):
    book_to_display =Book.objects.get(id = num)
    logged_in_user = User.objects.get(id=request.session['user_id'])
    context = {
        "logged_in_user": logged_in_user,
        "book_to_display": Book.objects.get(id = num)
    }
    return render(request,'books.html',context)
def removefav(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    fav_book = Book.objects.get(id =request.POST['book_id'])
    logged_in_user.liked_books.remove(fav_book)
    return redirect('/books')
def editbook(request):
    book_to_edit = Book.objects.get(id=request.POST['book_id'])
    num = book_to_edit.id
    book_to_edit.title = request.POST['title']
    book_to_edit.desc = request.POST['desc']
    book_to_edit.save()
    return redirect(f'/books/{num}')
