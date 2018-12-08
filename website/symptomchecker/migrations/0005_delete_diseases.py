# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptomchecker', '0004_diseases_symptoms'),
    ]

    operations = [
        migrations.DeleteModel(
            name='diseases',
        ),
    ]
