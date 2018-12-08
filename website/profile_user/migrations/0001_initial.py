# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=250)),
                ('last_name', models.CharField(default=b'', max_length=250)),
                ('email_id', models.CharField(default=b'', max_length=500)),
                ('DateofBirth', models.DateField(null=True)),
                ('password', models.CharField(default=b'', max_length=250)),
                ('gender', models.CharField(default=b'', max_length=10)),
                ('address', models.CharField(default=b'', max_length=100)),
                ('city', models.CharField(default=b'', max_length=100)),
                ('state', models.CharField(default=b'', max_length=100)),
                ('zip', models.CharField(default=b'', max_length=25)),
                ('phonen', models.CharField(default=b'', max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
