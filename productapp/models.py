#encoding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# ------------------------------------------------------------------------------
## 地区
class District(models.Model):
    code = models.PositiveIntegerField(primary_key=True, unique=True, verbose_name=u'地区编码', max_length=6, blank=False, null=False)
    name = models.CharField(max_length=6, verbose_name=u'地区名称', blank=False, null=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'地区名称'
        verbose_name_plural = u'地区列表'

## 居民小区
class Community(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name=u'小区名称', blank=False, null=False)
    district = models.ForeignKey(District, verbose_name=u'所在地区', related_name='communities')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'小区名称'
        verbose_name_plural = u'小区列表'

# ------------------------------------------------------------------------------
'''
class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=u'产品类别')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'产品类别'
        verbose_name_plural = u'产品类别列表'
'''
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=u'产品名称')
    #category = models.ForeignKey(ProductCategory, verbose_name=u'产品类别')
    description = models.TextField(verbose_name=u'产品描述')
    origin_place = models.CharField(max_length=10, verbose_name=_(u'产地'))
    thumb_image = models.URLField(max_length=100, verbose_name=u'略缩图链接')
    on_sale_communities = models.ManyToManyField(Community, related_name='products', verbose_name=u'在售小区列表')
    original_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u'产品原价')
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u'折扣价', blank=True, null=True)
    datetime_available = models.DateTimeField(verbose_name=_(u'上架时间'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'产品信息'
        verbose_name_plural = u'产品列表'

class Image(models.Model):
    name = models.ForeignKey(Product, verbose_name=u'产品名称')
    url = models.URLField(max_length=100, verbose_name=u'图片链接')

    def __unicode__(self):
        return self.url

    class Meta:
        verbose_name = u'图片链接'
        verbose_name_plural = u'图片链接列表'
