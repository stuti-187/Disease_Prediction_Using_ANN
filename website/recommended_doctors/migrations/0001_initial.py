# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=500)),
                ('type', models.CharField(default=b'', max_length=250)),
                ('hospital_name', models.CharField(default=b'', max_length=500)),
                ('monday', models.CharField(default=b'', max_length=500)),
                ('tuesday', models.CharField(default=b'', max_length=500)),
                ('wednesday', models.CharField(default=b'', max_length=500)),
                ('thursday', models.CharField(default=b'', max_length=500)),
                ('friday', models.CharField(default=b'', max_length=500)),
                ('saturday', models.CharField(default=b'', max_length=500)),
                ('sunday', models.CharField(default=b'', max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
