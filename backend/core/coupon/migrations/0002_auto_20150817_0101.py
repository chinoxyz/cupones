# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basecoupon',
            name='company',
            field=models.ForeignKey(to='company.Company', null=True),
        ),
    ]
