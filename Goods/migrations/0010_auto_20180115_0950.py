# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0009_auto_20180113_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='receiver_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='telephone',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='color',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='size',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
