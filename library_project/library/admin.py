from django.contrib import admin
from .models import Book, Author

class BookInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'nationality')
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('nationality',)
    inlines = [BookInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    ordering = ('title', 'publication_year')
    list_filter = ('publication_year', 'author')
