# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0013_auto_20180115_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='pic_url',
            field=models.CharField(max_length=500),
        ),
    ]
