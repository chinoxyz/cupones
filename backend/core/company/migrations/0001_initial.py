# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '__first__'),
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('phones', models.CharField(max_length=256, null=True, blank=True)),
                ('webpage', models.CharField(max_length=256, null=True, blank=True)),
                ('info', models.TextField(null=True, blank=True)),
                ('location', models.ForeignKey(default=None, blank=True, to='location.Location', null=True)),
                ('user', models.ForeignKey(related_name='owner', to='user.AppUser')),
            ],
        ),
    ]
