# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptomchecker', '0007_auto_20161003_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseases_symptoms',
            name='age_group',
            field=models.CharField(max_length=250, verbose_name=(b'Newborn (0-28 days)', b'Infant (29 days-1 year)', b'Younger Child (1 year-5 years)', b'Older Child (6-12 years)', b'Adolescent (13-16 years)', b'Young Adult (17-29 years)', b'Adult (30-39 years)', b'Adult (40-49 years)', b'Adult (50-64 years)', b'Senior (65 years-over)')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diseases_symptoms',
            name='gender',
            field=models.CharField(default=b'none', max_length=5, verbose_name=(b'Male', b'Female')),
            preserve_default=True,
        ),
    ]
