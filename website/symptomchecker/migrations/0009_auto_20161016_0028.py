# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptomchecker', '0008_auto_20161016_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseases_symptoms',
            name='age_group',
            field=models.CharField(max_length=250),
            preserve_default=True,
        ),
    ]
