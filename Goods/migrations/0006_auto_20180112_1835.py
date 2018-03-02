# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0005_auto_20180112_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='commodity_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='pic_url',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='receiver_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
