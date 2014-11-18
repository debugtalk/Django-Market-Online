# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('code', models.PositiveIntegerField(max_length=6, unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField()),
                ('original_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('current_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('datetime_available', models.DateTimeField(verbose_name='available datetime')),
                ('areas', models.ManyToManyField(to='productapp.Area')),
                ('images', models.ManyToManyField(to='productapp.Image')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
