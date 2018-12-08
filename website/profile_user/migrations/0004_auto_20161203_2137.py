# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_user', '0003_auto_20161203_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='any_congential',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_details',
            name='surgery_accident',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
    ]
