
from django.db import models
from django.db.models.fields import CharField, FloatField, DateTimeField,\
    TextField, IntegerField
from django.db.models.fields.related import ForeignKey

from backend.backend.models.company.models import Company
from backend.backend.models.user.models import AppUser


class BaseCoupon(models.Model):
    company = ForeignKey(Company)
    title = CharField(max_length = 120)
    price = FloatField()
    creation_date = DateTimeField(auto_now_add=True)
    modification_date= DateTimeField(auto_now=True)
    details = TextField()
    conditions = TextField()
    information = TextField()
    expiration_date = DateTimeField()

class Coupon(models.Model):
    creation_date= DateTimeField(auto_now_add=True)
    basecoupon = ForeignKey(BaseCoupon)
    user = ForeignKey(AppUser)
    status = IntegerField()
    rating = FloatField()