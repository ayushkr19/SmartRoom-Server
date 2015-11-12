# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartroomapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='author',
            field=models.CharField(default='ayush', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='title',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
