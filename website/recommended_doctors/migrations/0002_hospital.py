# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommended_doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=500)),
                ('address', models.CharField(default=b'', max_length=500)),
                ('city', models.CharField(default=b'', max_length=500)),
                ('state', models.CharField(default=b'', max_length=500)),
                ('zip', models.CharField(default=b'', max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
