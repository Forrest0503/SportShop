# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0004_auto_20180111_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='picture',
            field=models.ImageField(upload_to=b'goods_img/'),
        ),
    ]
