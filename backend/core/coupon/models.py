
from django.db import models
from django.db.models.fields import CharField, FloatField, DateTimeField,\
    TextField, IntegerField
from django.db.models.fields.related import ForeignKey

from backend.core.company.models import Company
from backend.core.user.models import AppUser


class BaseCoupon(models.Model):
    company = ForeignKey(Company, null=True)
    title = CharField(max_length=120)
    price = FloatField()
    creation_date = DateTimeField(auto_now_add=True)
    modification_date = DateTimeField(auto_now=True)
    details = TextField()
    conditions = TextField()
    information = TextField()
    expiration_date = DateTimeField()

    def __unicode__(self):
        return self.title


class Coupon(models.Model):
    creation_date = DateTimeField(auto_now_add=True)
    basecoupon = ForeignKey(BaseCoupon)
    user = ForeignKey(AppUser)
    status = IntegerField()
    rating = FloatField()

    def __unicode__(self):
        return str(self.basecoupon)
