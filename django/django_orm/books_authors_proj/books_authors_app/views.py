from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    context = {
        "all_books" :Book.objects.all(),
    }
    return render(request,"index.html",context)
def submit_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['description'],
    )
    return redirect("/")
def auths(request):
    context = {
        "all_authors" : Author.objects.all()
    }
    return render(request,"authors.html",context)

def submit_auth(request):
    Author.objects.create(
        first_name = request.POST['first'],
        last_name = request.POST['last'],
        notes = request.POST['notes'],
    )
    return redirect("/authors")
def book_page(request, num):
    book_to_show = Book.objects.get(id = num)
    context = {
        "all_authors" : Author.objects.all(),
        "book_to_show" :Book.objects.get(id = num),
        "book_authors": book_to_show.authors.all()
    }
    return render(request, 'books.html',context)
def add_auth(request):
    book = Book.objects.get(id =request.POST['book_id'])
    author = Author.objects.get(id= request.POST['auth_id'])
    book.authors.add(author)
    return redirect(f"/books/{book.id}")
def auth_page(request,num):
    auth_to_show = Author.objects.get(id = num)
    context = {
        "all_books": Book.objects.all(),
        "auth_to_show": Author.objects.get(id = num),
        "auth_books": auth_to_show.books.all()
    }
    return render(request,'auth_display.html',context)
def add_book(request):
    author = Author.objects.get(id=request.POST['auth_id'])
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect(f"/authors/{author.id}")