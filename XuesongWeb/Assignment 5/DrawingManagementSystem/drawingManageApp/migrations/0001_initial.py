# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DrawingID', models.CharField(max_length=10)),
                ('BuildingName', models.CharField(max_length=20)),
                ('ConstructedYear', models.IntegerField()),
                ('Contractor', models.CharField(max_length=20)),
                ('Floor', models.CharField(max_length=4)),
                ('Shop', models.CharField(max_length=10)),
            ],
        ),
    ]
