from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.
from productapp.models import Product
from datetime import datetime

def hello(request):
    return HttpResponse("hello, Products!")

def list_product(request):
    list_items = Product.objects.all()
    #list_items = Product.objects.filter(date_available__lt=datetime.now().datetime()).order_by("-date_available")
    paginator = Paginator(list_items, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)
    return render(request, 'productapp/list_product.html', locals())

def view_product(request, id):
    product = Product.objects.get(id = id)
    return render(request, 'productapp/view_product.html', locals())
