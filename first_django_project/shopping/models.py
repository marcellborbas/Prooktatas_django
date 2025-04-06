from django.db import models

class Customer(models.Model):
    obecjts = None
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    expiry_date = models.DateField(blank=True, null=True)
    is_discounted = models.BooleanField(default=False)
    storage_quantity = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.name} {self.price}'
