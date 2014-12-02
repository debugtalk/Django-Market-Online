#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from productapp.models import Product
from cartapp.cart import Cart, CART_SESSION_KEY
import json

def show_cart(request):
    cart = Cart(request.session)
    cart_json = cart.session[CART_SESSION_KEY]
    productList = []
    for product_id in cart_json:
        product_quantity = cart_json[product_id]['quantity']
        product = {'obj':Product.objects.get(id=product_id), 'quantity':product_quantity}
        productList.append(product)
    return render(request, 'cart.html', locals())

def add_product_to_cart(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    quantity = request.POST.get('quantity', 1)
    cart.add_product_to_cart(product, quantity)
    resp_json = json.dumps(cart.items_serialized_dict)
    return HttpResponse(resp_json)

def remove_productCategory_from_cart(request, product_id):
    cart = Cart(request.session)
    product = Product.objects.get(id=product_id)
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

def update_quantity(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    quantity = request.POST.get('quantity')
    cart.set_quantity(product, quantity)
    return HttpResponse(cart.total)

def get_cart_total_price(request):
    cart = Cart(request.session)
    return HttpResponse(cart.total)

def log_user_info(request):
    if request.method == 'POST':
        #address = request.REQUEST['address']
        return HttpResponseRedirect('/cart/success/')
    else:
        return render(request, 'order.html', locals())

def order_successfully(request):
    #request.session['tempSession'] = {}
    return render(request, 'order_success.html')

def confirm_order(request):
    cart = Cart(request.session)
    cart_info = json.dumps(cart.items_serialized_dict)
