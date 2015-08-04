# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twisi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twisser',
            name='twissies',
            field=models.IntegerField(default=0),
        ),
    ]
