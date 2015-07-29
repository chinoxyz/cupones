from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey

from backend.backend.models.user.models import AppUser


class Company(models.Model):
    user = ForeignKey(AppUser)
    location = ForeignKey(default=None, blank=True, null=True)
    
    name = CharField(max_length=100)
    creation_date= DateTimeField(auto_now_add=True)
    modification_date= DateTimeField(auto_now=True)
    phones = CharField(max_length = 256, blank=True, null=True)
    webpage = CharField(max_length = 256, blank=True, null=True)
    info = TextField( blank=True, null=True)
    