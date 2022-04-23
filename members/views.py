from members.forms import CreateAuthorForm, CreateBookForm, EditBookForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from multiprocessing import context
import os
from .models import Book ,Author




def index(request):
    context ={
        "books":Book.objects.all()
    }
    return render(request,"books/welcome.html", context=context)
# Create your views here.


def bookDetails (request , bookId):
    book = get_object_or_404(Book , id = bookId)
    image=  os.path.basename(book.image.__str__())
    context={
        "book" : book,
        "image" :image
    }
    return render (request,"books/index.html",context=context)


def authorDetails (request , authorId):
    author = get_object_or_404(Author , id = authorId)
    
    book = Book.objects.filter(Author_id = authorId).all()
    number_of_books=len(book)
    context={
        "books" : book,
        "author" : author,
        "number_of_books":number_of_books
    }
    return render (request,"books/authorDetails.html",context=context)


def createBook (request):
    if request.method == "POST":
        form = CreateBookForm(request.POST , request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            publish_date=form.cleaned_data['publish_date']
            add_to_site=form.cleaned_data['add_to_site']
            author=form.cleaned_data['author']
            price=form.cleaned_data['price']
            appropriate=form.cleaned_data['appropriate']
            # image=form.cleaned_data['image']
            book=Book.objects.create(name=name, publish_date=publish_date, add_to_site=add_to_site, Author=author,price=price, appropriate=appropriate )
            # book=form.save()
            return redirect("books")
    else:
     form = CreateBookForm(request.POST)
    return render(request,"books/createBook.html",context={"form":form})

def createAuthor (request):
    if request.method == "POST":
        forms = CreateAuthorForm (request.POST)
        if forms.is_valid():
            name=forms.cleaned_data['name']
            author=Author.objects.create(name=name)
            return redirect("books")
    else:
     forms = CreateAuthorForm()
    return render(request,"books/createAuthor.html",context={"forms":forms})

def removeBook(request,book_id):
    book = Book.objects.filter(id = book_id).delete()
    return redirect("books")

def editBook (request,book_id):
    book= get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = EditBookForm(request.POST , instance=book)
        if form.is_valid():
            book=form.save()
            return redirect('book_list' , bookId=book.id)
    else:
     form = EditBookForm(instance=book)
    return render(request,"books/createBook.html",context={"form":form})






    """
    def welcome(request):
        return render(request, "members/welcome.html")
    """

    
    """
    books = [
    {"name":"book psychology", "id":1, "description":" this is the description of book1", "image":"11.jpg"}, 
    {"name":"book history", "id":2, "description":" this is the description of book2", "image":"12.png"},
    {"name":"book science", "id":3, "description":" this is the description of book3", "image":"14.jpg"}
    ]
    """
    
    """
    def memberWelcome(request, num):
        return HttpResponse(f"Welcome book {num}")
    """

    
    
    """
    def bookWelcome(request, num):
        book=next(item for item in books if item["id"] == num)
    context ={
        "book":book
    }
    return render(request, "books/index.html", context=context)
    
    """
    
    """
    author details 
    # book= Book.objects.first().Author_id.all()
    # book= Book.objects.get(Author_id = authorId).get_all_objects()
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    """