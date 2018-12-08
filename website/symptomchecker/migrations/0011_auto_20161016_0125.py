# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptomchecker', '0010_auto_20161016_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseases_symptoms',
            name='gender',
            field=models.CharField(default=b'none', max_length=10, verbose_name=(b'Male', b'Female')),
            preserve_default=True,
        ),
    ]
