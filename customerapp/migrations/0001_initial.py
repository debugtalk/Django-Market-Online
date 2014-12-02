# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=6, verbose_name='\u7528\u6237\u59d3\u540d')),
                ('wx_openid', models.CharField(max_length=28, verbose_name='\u5fae\u4fe1ID')),
                ('phone_number', models.CharField(max_length=15, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('address', models.CharField(max_length=30, verbose_name='\u8be6\u7ec6\u4f4f\u5740')),
                ('email', models.EmailField(max_length=20, null=True, verbose_name='\u7535\u5b50\u90ae\u7bb1', blank=True)),
                ('status', models.CharField(max_length=10, verbose_name='\u7528\u6237\u72b6\u6001', choices=[(b'Following', '\u5df2\u5173\u6ce8'), (b'Gone', '\u53d6\u6d88\u5173\u6ce8')])),
                ('community', models.ForeignKey(related_name='customers', verbose_name='\u6240\u5728\u5c0f\u533a', to='productapp.Community')),
            ],
            options={
                'verbose_name': '\u987e\u5ba2\u4fe1\u606f',
                'verbose_name_plural': '\u987e\u5ba2\u4fe1\u606f\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_price', models.DecimalField(verbose_name='\u8ba2\u5355\u603b\u4ef7', max_digits=6, decimal_places=2)),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0b\u5355\u65f6\u95f4')),
                ('confirm_time', models.DateTimeField(auto_now_add=True, verbose_name='\u786e\u8ba4\u65f6\u95f4')),
                ('status', models.CharField(max_length=10, verbose_name='\u8ba2\u5355\u72b6\u6001', choices=[(b'Success', '\u4e0b\u5355\u6210\u529f'), (b'Cancel', '\u8ba2\u5355\u53d6\u6d88'), (b'Fail', '\u8ba2\u5355\u5931\u8d25')])),
                ('transaction_mode', models.CharField(max_length=15, verbose_name='\u4ea4\u6613\u65b9\u5f0f', choices=[(b'CashOnDelivery', '\u8d27\u5230\u4ed8\u6b3e'), (b'Alipay', '\u652f\u4ed8\u5b9d'), (b'Tenpay', '\u8d22\u4ed8\u901a'), (b'NetBank', '\u7f51\u94f6')])),
                ('remark', models.TextField(max_length=50, verbose_name='\u5907\u6ce8\u4fe1\u606f')),
                ('customer', models.ForeignKey(related_name='orders', verbose_name='\u987e\u5ba2\u59d3\u540d', to='customerapp.Customer')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u4fe1\u606f',
                'verbose_name_plural': '\u8ba2\u5355\u4fe1\u606f\u5217\u8868',
            },
            bases=(models.Model,),
        ),
    ]
