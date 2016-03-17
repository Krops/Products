# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=django_prices.models.PriceField(currency='USD', decimal_places=2, max_digits=9, verbose_name='Price'),
        ),
    ]
