# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0010_auto_20180115_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='color',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopping',
            name='size',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='size',
            field=models.CharField(max_length=50),
        ),
    ]
