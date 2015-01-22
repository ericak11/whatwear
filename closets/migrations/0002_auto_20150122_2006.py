# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('closets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='user',
        ),
        migrations.AlterField(
            model_name='closet',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
