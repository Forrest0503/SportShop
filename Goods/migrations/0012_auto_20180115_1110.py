# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0011_auto_20180115_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='color',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='size',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='color',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='size',
            field=models.CharField(max_length=200),
        ),
    ]
