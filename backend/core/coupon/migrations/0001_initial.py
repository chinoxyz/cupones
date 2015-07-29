# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '__first__'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCoupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('price', models.FloatField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('details', models.TextField()),
                ('conditions', models.TextField()),
                ('information', models.TextField()),
                ('expiration_date', models.DateTimeField()),
                ('company', models.ForeignKey(to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField()),
                ('rating', models.FloatField()),
                ('basecoupon', models.ForeignKey(to='coupon.BaseCoupon')),
                ('user', models.ForeignKey(to='user.AppUser')),
            ],
        ),
    ]
