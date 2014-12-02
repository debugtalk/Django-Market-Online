#encoding:utf-8
from django.db import models

# Create your models here.
from productapp.models import Community
# ------------------------------------------------------------------------------
## 用户信息
class Customer(models.Model):
    name = models.CharField(max_length=6, verbose_name=u'用户姓名', blank=False, null=False)
    wx_openid = models.CharField(max_length=28, verbose_name=u'微信ID', blank=False, null=False)
    phone_number = models.CharField(max_length=15, verbose_name=u'手机号码', blank=False, null=False)
    community = models.ForeignKey(Community, verbose_name=u'所在小区', related_name='customers')
    address = models.CharField(max_length=30, verbose_name=u'详细住址', blank=False, null=False)
    email = models.EmailField(max_length = 20, verbose_name=u'电子邮箱', blank=True, null=True)
    User_STATUS = (
        ('Following', u'已关注'),
        ('Gone', u'取消关注'),
    )
    status = models.CharField(max_length=10, choices=User_STATUS, verbose_name=u'用户状态')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'顾客信息'
        verbose_name_plural = u'顾客信息列表'

## 订单信息
class Order(models.Model):
    customer = models.ForeignKey(Customer, verbose_name=u'顾客姓名', related_name='orders')
    #detail = 
    total_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u'订单总价', blank=False, null=False)
    order_time = models.DateTimeField(verbose_name=u'下单时间', auto_now_add=True)
    confirm_time = models.DateTimeField(verbose_name=u'确认时间', auto_now_add=True)
    ORDER_STATUS = (
        ('Success', u'下单成功'),
        ('Cancel', u'订单取消'),
        ('Fail', u'订单失败'),
    )
    status = models.CharField(max_length=10, choices=ORDER_STATUS, verbose_name=u'订单状态')
    TRANSCATION_MODE = (
        ('CashOnDelivery', u'货到付款'),
        ('Alipay', u'支付宝'),
        ('Tenpay', u'财付通'),
        ('NetBank', u'网银'),
    )
    transaction_mode = models.CharField(max_length=15, choices=TRANSCATION_MODE, verbose_name=u'交易方式')
    remark = models.TextField(max_length=50, verbose_name=u'备注信息', blank=False, null=False)

    def __unicode__(self):
        return self.time

    class Meta:
        verbose_name = u'订单信息'
        verbose_name_plural = u'订单信息列表'
