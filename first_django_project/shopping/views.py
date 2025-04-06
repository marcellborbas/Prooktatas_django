from idlelib.editor import keynames

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import CustomerForm, ProductForm, ProductForm2
from .models import Customer, Product


# Create your views here.


def index(request):
    #return HttpResponse("Welcome to the shopping page!")
    return render(request, 'shopping/index.html')


def get_customers(request):
    print(request.GET)
    print(request.POST)
    customers = Customer.objects.all()
    form = CustomerForm(request.GET or None)
    print('DATA', form.data)
    if request.GET and form.is_valid():
        print('CLEANED', form.cleaned_data)
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        customers = customers.filter(
            first_name__contains=first_name,
            last_name__contains=last_name,
            email__contains=email
        )

    context = {
        'form': form,
        'customers': customers
    }
    return render(request, 'shopping/customers.html', context)



def get_products(request):
    products = Product.objects.all()
    form = ProductForm(request.GET or None)
    print(form.data)
    if form.is_valid():
        print(form.cleaned_data)
        product_name = form.cleaned_data.get('name')
        price_lower = form.cleaned_data.get('price_limit_lower')
        price_higher = form.cleaned_data.get('price_limit_higher')
        #price = form.cleaned_data.get('price')
        #products = products.filter(name__contains=product_name, price__contains=price)
        products = products.filter(
            name__contains=product_name,
            price__gte=price_lower,
            price__lte=price_higher,
        )
    context = {'products': products, 'form': form}
    return render(request, 'shopping/products.html', context)



def get_product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse("No product found", status=404)

    context = {'product': product}
    return render(request, 'shopping/product_details.html', context)



def get_customer_details(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return HttpResponse("No customer found", status=404)

    context = {'customer': customer}
    return render(request, 'shopping/customer_details.html', context)
