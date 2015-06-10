# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wxpoint', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelRun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('run_name', models.TextField(max_length=20)),
                ('currmodel', models.ForeignKey(to='wxpoint.NModels')),
            ],
        ),
    ]
