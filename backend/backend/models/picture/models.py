from django.db import models
from django.db.models.fields import FloatField, CharField, DateTimeField


class Photo(models.Model):
    url = CharField(max_length = 256)
    creation_date= DateTimeField(auto_now_add=True)