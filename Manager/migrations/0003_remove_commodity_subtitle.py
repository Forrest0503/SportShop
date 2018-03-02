# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0002_commodity_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='subtitle',
        ),
    ]
