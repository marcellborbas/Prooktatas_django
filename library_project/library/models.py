from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    page_count = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.author})"
