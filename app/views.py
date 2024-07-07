from django.shortcuts import render,redirect
from .models import *
from .forms import BookForm , CategoryForm

def index(request):
    if request.method == "POST":
        add_book = BookForm(request.POST , request.FILES)
        add_cat = CategoryForm(request.POST)
        if add_book.is_valid():
            add_book.save()
            
        if add_cat.is_valid():
            add_cat.save()
    
    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
        'form': BookForm(),
        'formCat': CategoryForm(),
        'allbooks': Book.objects.filter(active = True).count(),
        'soldbooks': Book.objects.filter(status = 'sold').count(),
        'rentedbooks': Book.objects.filter(status = 'rented').count(),
        'avilablebooks': Book.objects.filter(status = 'avilable').count(),
    }
    return render(request ,'pages/index.html' , context)

def books(request):
    search =  Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains = title)
    
    
    context = {
        'category': Category.objects.all(),
        'books': search,
        'formCat': CategoryForm(),
    }
    return render(request ,'pages/books.html',context)

def Update(request , id):
    book_id = Book.objects.get(id = id)
    
    if request.method == 'POST':
        book_save = BookForm(request.POST , request.FILES , instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
    context = {
        'form':book_save,
    }
    return render(request, 'pages/update.html' , context)

def Delete(request , id):
    book_id = Book.objects.get(id = id)
    
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')

