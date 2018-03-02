# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0007_auto_20180113_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='color',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='size',
            field=models.CharField(max_length=200),
        ),
    ]
