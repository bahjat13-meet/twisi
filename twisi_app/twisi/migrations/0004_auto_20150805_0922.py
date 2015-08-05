# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twisi', '0003_drawing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drawing',
            name='user',
        ),
        migrations.AddField(
            model_name='drawing',
            name='twisser',
            field=models.ForeignKey(default=0, to='twisi.Twisser'),
            preserve_default=False,
        ),
    ]
