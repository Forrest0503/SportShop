# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0006_auto_20180113_0816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commodity',
            options={'ordering': ['-id']},
        ),
    ]
