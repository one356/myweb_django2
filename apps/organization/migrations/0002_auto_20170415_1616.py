# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-15 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citydict',
            options={'verbose_name': '\u57ce\u5e02', 'verbose_name_plural': '\u57ce\u5e02'},
        ),
        migrations.AlterModelOptions(
            name='courseorg',
            options={'verbose_name': '\u8bfe\u7a0b\u673a\u6784', 'verbose_name_plural': '\u8bfe\u7a0b\u673a\u6784'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '\u6559\u5e08', 'verbose_name_plural': '\u6559\u5e08'},
        ),
    ]
