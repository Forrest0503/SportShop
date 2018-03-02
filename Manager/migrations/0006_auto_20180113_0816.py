# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0005_auto_20180111_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
