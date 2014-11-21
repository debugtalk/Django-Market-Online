#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from productapp.models import Product
from cartapp.cart import Cart, CART_SESSION_KEY

def show_cart(request):
    cart = Cart(request.session)
    cart_json = cart.session[CART_SESSION_KEY]
    return HttpResponse(cart_json)
    #return render(request, 'cartapp/test.html', locals())

def add_product_to_cart(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    quantity = request.POST.get('quantity', 1)
    cart.add_product_to_cart(product, quantity)
    #return show_cart(request)
    return HttpResponse()

def remove_productCategory_from_cart(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    cart.remove_productCategory_from_cart(product)
    return show_cart(request)

def remove_prodcutItem_from_cart(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    cart.remove_prodcutItem_from_cart(product)
    return show_cart(request)

def clear_cart(request):
    cart = Cart(request.session)
    cart.clear()
    return show_cart(request)

def set_quantity(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    quantity = request.POST.get('quantity')
    cart.set_quantity(product, quantity)
    return HttpResponse()