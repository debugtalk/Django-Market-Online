#encoding:utf-8
from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from models import Product, CartItem
from forms import ProductForm
from datetime import datetime

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    return render(request, 'marketapp/create_product.html', locals())

def list_product(request):
    list_items = Product.objects.all()
    paginator = Paginator(list_items, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)
    return render(request, 'marketapp/list_product.html', locals())

def view_product(request, id):
    product_instance = Product.objects.get(id = id)
    return render(request, 'marketapp/view_product.html', locals())

def edit_product(request, id):
    product_instance = Product.objects.get(id = id)
    form = ProductForm(request.POST or None, instance = product_instance)
    if form.is_valid():
        form.save()
    return render(request, 'marketapp/edit_product.html', locals())

class Cart(object):
    def __init__(self, *args, **kwargs):
        self.items = []
        self.total_price = 0

    def add_product(self, product):
        self.total_price += product.price
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += 1
                return
        cart_item = CartItem(product=product, unit_price=product.price, quantity=1)
        self.items.append(cart_item)

import pickle

def view_cart(request):
    cart = request.session.get('cart', None)
    if not cart:
        cart = Cart()
    else:
        cart = pickle.loads(cart)
    return render(request, 'marketapp/view_cart.html', locals())

def add_to_cart(request, id):
    product = Product.objects.get(id = id)
    cart = request.session.get('cart', None)
    if not cart:
        cart = Cart()
    else:
        cart = pickle.loads(cart)
    cart.add_product(product)
    request.session['cart'] = pickle.dumps(cart)
    return view_cart(request)

def clean_cart(request):
    request.session['cart'] = pickle.dumps(Cart())
    return view_cart(request)

def store_view(request):
    products = Product.objects.filter(date_available__lt=datetime.now().date()).order_by("-date_available")
    return render(request, 'marketapp/store.html', locals())
