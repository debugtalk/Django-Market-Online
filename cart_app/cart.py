from datetime import datetime
from cartapp.models import Cart, CartItem

CART_ID = 'cart_id'

class ItemAlreadyExists(Exception):
    pass

class ItemDoesNotExist(Exception):
    pass

class Cart(object):
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = Cart.objects.get(id=cart_id, checked_out=False)
            except Cart.DoesNotExist:
                cart = self.init_cart(request)
        else:
            cart = self.init_cart(request)
        self.cart = cart

    def init_cart(self, request):
        cart = Cart()
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product, quantity=1):
        try:
            item = CartItem.objects.get(
                cart=self.cart,
                product=product,
            )
        except CartItem.DoesNotExist:
            item = CartItem()
            item.cart = self.cart
            item.product = product
            item.unit_price = product.current_price
            item.quantity = quantity
            item.save()
        else: #ItemAlreadyExists
            item.unit_price = product.current_price
            item.quantity = item.quantity + int(quantity)
            item.save()

    def remove(self, product):
        try:
            item = CartItem.objects.get(
                cart=self.cart,
                product=product,
            )
        except CartItem.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()

    def count(self):
        num = 0
        for item in self.cart.cartitem_set.all():
            num += 1 * item.quantity
        return num

    def total_price(self):
        total = 0
        for item in self.cart.cartitem_set.all():
            total += item.total_price
        return total

    def clear(self):
        for item in self.cart.cartitem_set.all():
            item.delete()

'''
    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item
'''