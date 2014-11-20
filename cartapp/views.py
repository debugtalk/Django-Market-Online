#encoding:utf-8
from django.shortcuts import render

# Create your views here.
from cartapp.cart import Cart, CART_SESSION_KEY
from productapp.models import Product

def view_cart(request):
    cart = Cart(request.session)
    items = cart.items
    products = cart.products
    return render(request, 'cartapp/test.html', locals())

def add_to_cart(request, product_id, quantity=1):
    product = Product.objects.get(id=product_id)
    cart = Cart(request.session)
    cart.add(product, quantity)
    #request.session[CART_SESSION_KEY] = cart.id
    return view_cart(request)

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request.session)
    cart.remove(product)
    return view_cart(request)

def clean_cart(request):
    cart = Cart(request.session)
    cart.clear()
    return view_cart(request)

