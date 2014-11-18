from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# ------------------------------------------------------------------------------

class Area(models.Model):
    code = models.PositiveIntegerField(primary_key=True, max_length=6, unique=True, blank=False, null=False)
    name = models.CharField(max_length=6, unique=False, blank=False, null=False)

    def __unicode__(self):
        return self.name

# ------------------------------------------------------------------------------

class Image(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)

    def __unicode__(self):
        return self.name

# ------------------------------------------------------------------------------

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    images = models.ManyToManyField(Image)
    areas = models.ManyToManyField(Area)
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    current_price = models.DecimalField(max_digits=6, decimal_places=2)
    datetime_available = models.DateTimeField(verbose_name=_('available datetime'))

    def __unicode__(self):
        return self.name
