# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twisi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twisser',
            name='twissies',
            field=models.IntegerField(default=datetime.datetime(2015, 8, 3, 13, 47, 25, 378343, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
