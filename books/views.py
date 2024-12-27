from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
    # return JsonResponse(list(books), safe=False)

def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        isbn = request.POST['isbn']
        Book.objects.create(title=title, author=author, published_date=published_date, isbn=isbn)
        return redirect('book_list')
    return render(request, 'books/book_form.html')

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'book': book})

def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.isbn = request.POST['isbn']
        book.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'book': book})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})


