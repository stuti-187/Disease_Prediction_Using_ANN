# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommended_doctors', '0002_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='map_url',
            field=models.CharField(default=b'', max_length=5000),
            preserve_default=True,
        ),
    ]
