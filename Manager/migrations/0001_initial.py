# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('classify', models.IntegerField()),
                ('picture', models.ImageField(upload_to=b'')),
                ('inventory', models.IntegerField()),
                ('price', models.FloatField()),
                ('detail', models.CharField(max_length=1000)),
                ('onsale_time', models.DateField()),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('deleted', models.IntegerField()),
            ],
        ),
    ]
