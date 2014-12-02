# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10, verbose_name='\u5c0f\u533a\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u5c0f\u533a\u540d\u79f0',
                'verbose_name_plural': '\u5c0f\u533a\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('code', models.PositiveIntegerField(max_length=6, unique=True, serialize=False, verbose_name='\u5730\u533a\u7f16\u7801', primary_key=True)),
                ('name', models.CharField(max_length=6, verbose_name='\u5730\u533a\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u5730\u533a\u540d\u79f0',
                'verbose_name_plural': '\u5730\u533a\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=100, verbose_name='\u56fe\u7247\u94fe\u63a5')),
            ],
            options={
                'verbose_name': '\u56fe\u7247\u94fe\u63a5',
                'verbose_name_plural': '\u56fe\u7247\u94fe\u63a5\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('description', models.TextField(verbose_name='\u4ea7\u54c1\u63cf\u8ff0')),
                ('origin_place', models.CharField(max_length=10, verbose_name='\u4ea7\u5730')),
                ('thumb_image', models.URLField(max_length=100, verbose_name='\u7565\u7f29\u56fe\u94fe\u63a5')),
                ('original_price', models.DecimalField(verbose_name='\u4ea7\u54c1\u539f\u4ef7', max_digits=6, decimal_places=2)),
                ('discount_price', models.DecimalField(null=True, verbose_name='\u6298\u6263\u4ef7', max_digits=6, decimal_places=2, blank=True)),
                ('datetime_available', models.DateTimeField(verbose_name='\u4e0a\u67b6\u65f6\u95f4')),
                ('on_sale_communities', models.ManyToManyField(related_name='products', verbose_name='\u5728\u552e\u5c0f\u533a\u5217\u8868', to='productapp.Community')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u4fe1\u606f',
                'verbose_name_plural': '\u4ea7\u54c1\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.ForeignKey(verbose_name='\u4ea7\u54c1\u540d\u79f0', to='productapp.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='community',
            name='district',
            field=models.ForeignKey(related_name='communities', verbose_name='\u6240\u5728\u5730\u533a', to='productapp.District'),
            preserve_default=True,
        ),
    ]
