from django.contrib import admin
from .models import Customer, Product


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name', 'email', 'age']
    list_filter =  ['age']
    ordering = ['first_name']
    #fields = ['first_name', 'last_name', 'age']
    #readonly_fields = ['age']

fieldsets = (
    ('Name', {
        'fields': ('first_name', 'last_name')
    }),
    ('Contact information', {
        'fields': ('email', 'phone_number')
    }),
    ('Other', {
        'fields': ('age',)
    })
)

admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']

admin.site.register(Product, ProductAdmin)