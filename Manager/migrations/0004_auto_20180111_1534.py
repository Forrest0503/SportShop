# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0003_remove_commodity_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='classify',
            field=models.CharField(max_length=20),
        ),
    ]
