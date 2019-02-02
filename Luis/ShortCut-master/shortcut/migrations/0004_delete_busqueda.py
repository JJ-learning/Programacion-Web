# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortcut', '0003_busqueda'),
    ]

    operations = [
        migrations.DeleteModel(
            name='busqueda',
        ),
    ]
