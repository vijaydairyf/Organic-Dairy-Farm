# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0005_auto_20160925_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cattle',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
