#encoding:utf-8
from django.db import models
from django.contrib.contenttypes.models import ContentType

"""
The structure of a cart_instance shows below.
cart_instance
- cartItem1: product1 * num_1
- cartItem2: product2 * num_2

cart_instance.products = [product1, product2]
cart_instance.items = [cartItem1, cartItem2]

dict representation of cartItem shows below:
- cartItem1: {
       'product_pk': 1, # product1.pk = 1
       'quantity': 2, # number of product1 in the cart
       'unit_price': 15, # product1.price = 15
    }

- cartItem2:
  to_dict = {
       'product_pk': 2, # self.product.pk = 2
       'quantity': 3, # self['quantity'] = 3
       'unit_price': 18, # str(self.unit_price) = 18
    }
"""

class CartItem(object):
    """
    An item in cart, with the associated product and its quantity.
    For instance,
    """
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = int(quantity)
        self.unit_price = float(product.current_price)

    def __repr__(self):
        return u'CartItem Object (%s)' % self.product

    def to_dict(self):
        return {
            'product_pk': self.product.pk,
            'quantity': self.quantity,
            'unit_price': str(self.unit_price),
        }

CART_SESSION_KEY = 'CART'

class Cart(object):
    """
    A cart that lives in the session.
    """
    def __init__(self, session, session_key=None):
        self.items_serialized_dict = {}
        self.session = session
        self.session_key = session_key or CART_SESSION_KEY
        # If a cart representation was previously stored in session
        if self.session_key in self.session:
            # then we rebuild the cart object from that serialized representation.
            cart_representation = self.session[self.session_key]
            productIDs_in_cart = cart_representation.keys()
            product_instance = ContentType.objects.get(app_label="productapp", model="product")
            products_queryset = product_instance.model_class().objects.filter(pk__in=productIDs_in_cart)
            for product in products_queryset:
                cartItem = cart_representation[str(product.pk)]
                cartItem_instance = CartItem(product, cartItem['quantity'])
                self.items_serialized_dict[str(product.pk)] = cartItem_instance.to_dict()

    def is_contains(self, product):
        """
        Checks if the cart contains the given product.
        """
        return product in self.products

    def update_session(self):
        """
        Serializes the cart data, saves it to session and marks session as modified.
        """
        self.session[self.session_key] = self.items_serialized_dict
        self.session.modified = True

    def add_product_to_cart(self, product, quantity=1):
        """
        Adds or creates products in cart. For an existing product,
        the quantity is increased and the price is ignored.
        """
        quantity = int(quantity)
        if quantity < 1:
            raise ValueError('Quantity must be at least 1 when adding to cart')
        if product in self.products:
            self.items_serialized_dict[str(product.pk)]['quantity'] += quantity
        else:
            self.items_serialized_dict[str(product.pk)] = CartItem(product, quantity).to_dict()
        self.update_session()

    def set_quantity(self, product, quantity):
        """
        Sets the product's quantity.
        """
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError('Quantity must be positive when updating cart')
        elif quantity < 1: # quantity = 0
            del self.items_serialized_dict[str(product.pk)]
        else:
            if product in self.products:
                self.items_serialized_dict[str(product.pk)]['quantity'] = quantity
            else:
                self.items_serialized_dict[str(product.pk)] = CartItem(product, quantity).to_dict()
        self.update_session()

    def remove_productCategory_from_cart(self, product):
        """
        Removes the specified cartItem.
        """
        if product in self.products:
            del self.items_serialized_dict[str(product.pk)]
            self.update_session()

    def remove_prodcutItem_from_cart(self, product):
        """
        Removes a single product by decreasing the quantity.
        """
        if product in self.products:
            if self.items_serialized_dict[str(product.pk)]['quantity'] <= 1:
                # There's only 1 product left so we drop it
                del self.items_serialized_dict[str(product.pk)]
            else:
                self.items_serialized_dict[str(product.pk)]['quantity'] -= 1
            self.update_session()

    def clear(self):
        """
        Removes all items.
        """
        self.items_serialized_dict = {}
        self.update_session()

    """
    self.items_serialized_dict = {
        product1.pk: {'product_pk': product1.pk, 'quantity': num_1, 'unit_price': product1_price},
        product2.pk: {'product_pk': product2.pk, 'quantity': num_2, 'unit_price': product2_price},
    }
    """
    @property
    def items(self):
        """
        The list of cart items.
        For instance:
        cart_instance.keys = [1, 2]
        cart_instance.items = [
            {'product_pk': 1, 'quantity': 2, 'unit_price': 15},
            {'product_pk': 2, 'quantity': 3, 'unit_price': 18},
        ]
        """
        return self.items_serialized_dict.values()

    @property
    def products(self):
        """
        The list of associated products.
        For instance:
        cart_instance.products = [product1, product2]
        """
        products_list = []
        product_instance = ContentType.objects.get(app_label="productapp", model="product")
        product_class = product_instance.model_class() # Product
        for item in self.items:
            p = product_class.objects.get(pk=item['product_pk'])
            products_list.append(p)
        return products_list

    @property
    def count_of_products(self):
        """
        The number of products in cart, that's the sum of quantities.
        """
        return sum([item['quantity'] for item in self.items])

    @property
    def count_of_items(self):
        """
        The number of unique items in cart, regardless of the quantity.
        """
        return len(self.items_serialized_dict)

    @property
    def is_empty(self):
        return self.count_of_items == 0

    @property
    def total(self):
        """
        The total value of all products in the cart.
        """
        total = 0
        for item in self.items:
            subtotal = float(item['unit_price']) * int(item['quantity'])
            total += subtotal
        return total
