# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('map_type', models.TextField(max_length=20)),
                ('map_path', models.TextField(max_length=100)),
                ('timestep', models.TextField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ModelRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ModelRun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='NModels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mname', models.TextField(default='DEFVAL', max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='modelrun',
            name='currmodel',
            field=models.ForeignKey(to='wxpoint.NModels'),
        ),
        migrations.AddField(
            model_name='modelregion',
            name='model_run',
            field=models.ForeignKey(to='wxpoint.ModelRun'),
        ),
        migrations.AddField(
            model_name='modelimages',
            name='model_region',
            field=models.ForeignKey(to='wxpoint.ModelRegion'),
        ),
    ]
