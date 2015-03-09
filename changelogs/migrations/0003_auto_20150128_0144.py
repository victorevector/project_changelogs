# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changelogs', '0002_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changelog',
            name='date',
            field=models.CharField(help_text=b'Date: ', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='changelog',
            name='log',
            field=models.TextField(help_text=b'Log:   ', max_length=2000),
            preserve_default=True,
        ),
    ]
