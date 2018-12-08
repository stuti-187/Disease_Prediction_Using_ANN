# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinedata1',
            name='category',
            field=models.CharField(default=b'', max_length=250, null=True),
            preserve_default=True,
        ),
    ]
