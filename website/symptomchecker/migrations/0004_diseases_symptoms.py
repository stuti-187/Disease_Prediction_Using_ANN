# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptomchecker', '0003_auto_20160927_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases_Symptoms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disease', models.CharField(max_length=100)),
                ('symptom1', models.CharField(max_length=250)),
                ('symptom2', models.CharField(max_length=250)),
                ('symptom3', models.CharField(max_length=250)),
                ('symptom4', models.CharField(max_length=250)),
                ('symptom5', models.CharField(max_length=250)),
                ('symptom6', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
