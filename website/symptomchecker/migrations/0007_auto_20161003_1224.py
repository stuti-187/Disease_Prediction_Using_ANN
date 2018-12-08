# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptomchecker', '0006_auto_20161002_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseases_symptoms',
            name='age_from',
        ),
        migrations.RemoveField(
            model_name='diseases_symptoms',
            name='age_to',
        ),
        migrations.AddField(
            model_name='diseases_symptoms',
            name='age_group',
            field=models.CharField(default=b'choose age group', max_length=250),
            preserve_default=True,
        ),
    ]
