# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptomchecker', '0002_auto_20160927_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseases',
            name='symptoms',
            field=models.CharField(max_length=250),
            preserve_default=True,
        ),
    ]
