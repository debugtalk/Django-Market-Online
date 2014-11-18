#encoding:utf-8
from django.test import TestCase
from django.utils.translation import ugettext_lazy as _

# Create your tests here.

from productapp.models import Area, Image, Product
from datetime import datetime
from decimal import Decimal

class ProductAppModelsTestCase(TestCase):

    def test_create_area_in_database(self):
        area = Area()
        area.code = 101
        area.name = _(u'天河区')
        #area.save()
        return area

    def test_get_product_list(self):
        list_items = Product.objects.all()
        for item in list_items:
            print item.name
            print item.description

            image_urls = item.images.all()
            for url in image_urls:
                print url

            areas = item.areas.all()
            for area in areas:
                print area

            print item.original_price
            print item.current_price
            print item.datetime_available
