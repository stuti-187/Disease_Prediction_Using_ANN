# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='addict_hist',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='any_congential',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='asthma',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='blood_group',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='bronchites',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='diabetes',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='drug_allergy',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='drug_intake',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='fits',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='hypertension',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='other',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='psych_ill',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_details',
            name='surgery_accident',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
