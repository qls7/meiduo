# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-03 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='trade_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='支付编号'),
        ),
    ]
