# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='diseases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disease', models.CharField(max_length=100)),
                ('symptons', models.CharField(max_length=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
