# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0003_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='batch',
            field=models.IntegerField(null=True),
        ),
    ]
