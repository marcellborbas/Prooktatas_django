from django.shortcuts import render, get_object_or_404
from .models import Book, Author

def book_list(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__name__icontains=query)
    return render(request, 'library/book_list.html', {'books': books, 'query': query})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = author.books.all()
    return render(request, 'library/author_detail.html', {'author': author, 'books': books})
