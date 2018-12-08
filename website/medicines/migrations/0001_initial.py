# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medicinedata1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=250)),
                ('price', models.CharField(default=b'', max_length=500)),
                ('category', models.DateField(null=True)),
                ('quantity', models.CharField(default=b'', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
