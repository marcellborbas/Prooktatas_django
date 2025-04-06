from django.shortcuts import render
from .models import Book
from django.http import HttpResponseNotFound



def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'library/book_list.html', {'books': books, 'query': query})

def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponseNotFound("A könyv nem található.")

    return render(request, 'library/book_detail.html', {'book': book})