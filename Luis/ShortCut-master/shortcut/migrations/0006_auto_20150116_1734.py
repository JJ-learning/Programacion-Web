# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('shortcut', '0005_busqueda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to=b'', storage=django.core.files.storage.FileSystemStorage(location=b'/media/photos'), verbose_name=b'avatar_profile', blank=True),
            preserve_default=True,
        ),
    ]
