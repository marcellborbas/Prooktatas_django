from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    death_date = models.DateField(null=True, blank=True)
    death_place = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField()
    page_count = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"
