# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170328_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='disabled',
        ),
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False, help_text='\n            Designates whether user has verified email or not, different from is_active\n            because user can suspend his account, therefore changing the value of is_active by himself.\n        '),
        ),
    ]
