# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changelogs', '0003_auto_20150128_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changelog',
            name='date',
            field=models.DateField(help_text=b'Date: ', auto_now_add=True),
            preserve_default=True,
        ),
    ]
