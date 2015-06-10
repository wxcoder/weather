# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wxpoint', '0003_modelregion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('map_type', models.TextField(max_length=20)),
                ('map_path', models.TextField(max_length=20)),
                ('timestep', models.TextField(max_length=6)),
                ('model_region', models.ForeignKey(to='wxpoint.ModelRegion')),
            ],
        ),
    ]
