# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0008_auto_20180113_0923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopping',
            options={'ordering': ['-id']},
        ),
    ]
