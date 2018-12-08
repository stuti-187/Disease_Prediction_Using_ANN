# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptomchecker', '0005_delete_diseases'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseases_symptoms',
            name='age_from',
            field=models.IntegerField(default=0, max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diseases_symptoms',
            name='age_to',
            field=models.IntegerField(default=0, max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diseases_symptoms',
            name='gender',
            field=models.CharField(default=b'none', max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diseases_symptoms',
            name='is_pregnant',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
