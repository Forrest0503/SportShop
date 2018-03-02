# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('batch', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('date', models.DateField()),
                ('state', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.IntegerField()),
                ('commodity_id', models.IntegerField()),
                ('buying_price', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
