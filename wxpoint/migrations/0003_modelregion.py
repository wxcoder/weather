# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wxpoint', '0002_modelrun'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelRegion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('region', models.TextField(max_length=20)),
                ('model_run', models.ForeignKey(to='wxpoint.ModelRun')),
            ],
        ),
    ]
