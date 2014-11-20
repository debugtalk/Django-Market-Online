from django.db import models

# Create your models here.
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes.fields import GenericForeignKey
#from django.contrib.contenttypes import generic

class Cart(models.Model):
    #creation_datetime = models.DateTimeField(default=datetime.now(), verbose_name=_('creation datetime'))
    #checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

    def __init__(self):
        self.creation_datetime = models.DateTimeField(default=datetime.now(), verbose_name=_('creation datetime'))
        self.checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

    def __unicode__(self):
        return unicode(self.creation_datetime)

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        #ordering = ('-creation_datetime',)

class CartItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
            kwargs['object_id'] = kwargs['product'].pk
            del(kwargs['product'])
        return super(CartItemManager, self).get(*args, **kwargs)

class CartItem(models.Model):
    '''product items stored in cart'''
    cart = models.ForeignKey(Cart, verbose_name=_('cart'))
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('unit price'))
    # product as generic relation
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    #content_object = GenericForeignKey('content_type', 'object_id')

    objects = CartItemManager()

    class Meta:
        verbose_name = _('cart item')
        verbose_name_plural = _('cart items')
        ordering = ('cart',)

    def __unicode__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    def total_price(self):
        return self.quantity * self.unit_price

    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)



