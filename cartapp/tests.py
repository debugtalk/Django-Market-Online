from django.test import TestCase
from django.test import Client

# Create your tests here.
from django.core.urlresolvers import reverse
from productapp.models import Product
from datetime import datetime

class CartTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.product1 = Product.objects.create(name = 'product1', description = 'description1', original_price = 18, current_price = 15, datetime_available = datetime.now())
        self.product2 = Product.objects.create(name = 'product2', description = 'description2', original_price = 22, current_price = 19, datetime_available = datetime.now())
        self.url_add = reverse('cartapp:add_product_to_cart')
        self.url_show = reverse('cartapp:show_cart')
        self.url_remove = reverse('cartapp:remove_productCategory_from_cart')
        self.url_remove_single = reverse('cartapp:remove_prodcutItem_from_cart')
        self.url_quantity = reverse('cartapp:set_quantity')
        self.url_clear = reverse('cartapp:clear_cart')

    def test_product_is_added(self):
        post_data1 = {'product_id': self.product1.pk}
        post_data2 = {'product_id': self.product2.pk}
        self.client.post(self.url_add, post_data1)
        self.client.post(self.url_add, post_data2)
        response = self.client.get(self.url_show)
        print response.content
        #self.assertContains(response, '1')

    def test_show_cart(self):
        response = self.client.get(self.url_show)
        print response

    '''
    def test_multiple_products_are_added(self):
        self.client.post(self.url_add, self.deer_data)
        self.client.post(self.url_add, self.moose_data)
        response = self.client.get(self.url_show)
        self.assertContains(response, '1 deer for $10.0')
        self.assertContains(response, '1 moose for $20.0')

    def test_stale_item_is_removed_from_cart(self):
        # Items that are not anymore reference in the database should not be kept in cart.
        self.client.post(self.url_add, self.deer_data)
        self.client.post(self.url_add, self.moose_data)
        response = self.client.get(self.url_show)
        self.assertContains(response, 'deer')
        self.assertContains(response, 'moose')
        self.deer.delete()
        response = self.client.get(self.url_show)
        self.assertNotContains(response, 'deer')
        self.assertContains(response, 'moose')

    def test_quantity_increases(self):
        self.client.post(self.url_add, self.deer_data)
        self.deer_data['quantity'] = 2
        self.client.post(self.url_add, self.deer_data)
        response = self.client.get(self.url_show)
        self.assertContains(response, '3 deer')

    def test_items_are_counted_properly(self):
        self.deer_data['quantity'] = 2
        self.client.post(self.url_add, self.deer_data)
        self.client.post(self.url_add, self.moose_data)
        response = self.client.get(self.url_show)
        self.assertContains(response, 'items count: 3')
        self.assertContains(response, 'unique count: 2')

    def test_price_is_updated(self):
        # Let's give a discount: $1.5/product. That's handled on the test views.
        self.deer_data['quantity'] = 2
        self.deer_data['discount'] = 1.5
        self.client.post(self.url_add, self.deer_data)
        response = self.client.get(self.url_show)
        # subtotal = 10*2 - 1.5*2
        self.assertContains(response, '2 deer for $17.0')

    def test_products_are_removed_all_together(self):
        self.deer_data['quantity'] = 3
        self.client.post(self.url_add, self.deer_data)
        self.client.post(self.url_add, self.moose_data)
        remove_data = {'product_id': self.deer.pk}
        self.client.post(self.url_remove, remove_data)
        response = self.client.get(self.url_show)
        self.assertNotContains(response, 'deer')
        self.assertContains(response, 'moose')

    def test_single_product_is_removed(self):
        self.deer_data['quantity'] = 3
        self.client.post(self.url_add, self.deer_data)
        remove_data = {'product_id': self.deer.pk}
        self.client.post(self.url_remove_single, remove_data)
        response = self.client.get(self.url_show)
        self.assertContains(response, '2 deer')

    def test_quantity_is_overwritten(self):
        self.deer_data['quantity'] = 3
        self.client.post(self.url_add, self.deer_data)
        self.deer_data['quantity'] = 4
        self.client.post(self.url_quantity, self.deer_data)
        response = self.client.get(self.url_show)
        self.assertContains(response, '4 deer')

    def test_cart_items_are_cleared(self):
        self.client.post(self.url_add, self.deer_data)
        self.client.post(self.url_add, self.moose_data)
        self.client.post(self.url_clear)
        response = self.client.get(self.url_show)
        self.assertNotContains(response, 'deer')
        self.assertNotContains(response, 'moose')

    @override_settings(CART_PRODUCT_LOOKUP={'price__gt': 1})
    def test_custom_product_filter_are_applied(self):
        # We modify the queryset to exclude some products. For these excluded
        # we should not be able to add them in the cart.
        exclude = Product.objects.create(name='EXCLUDE', price=0.99, custom_id=100)
        exclude_data = {'product_id': exclude.pk}
        self.client.post(self.url_add, self.deer_data)
        self.client.post(self.url_add, exclude_data)
        response = self.client.get(self.url_show)
        self.assertNotContains(response, 'EXCLUDE')
        self.assertContains(response, 'deer')
'''