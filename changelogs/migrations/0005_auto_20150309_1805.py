# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changelogs', '0004_auto_20150128_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changelog',
            name='date',
            field=models.DateField(help_text=b'Date: '),
            preserve_default=True,
        ),
    ]
