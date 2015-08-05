from django.db import models
from django.db.models.fields import FloatField
from django.contrib.gis.geos import Point


class Location(models.Model):
    longitude = FloatField()
    latitude = FloatField()

    def set(self, x, y):
        self.longitude = x
        self.latitude = y
    
    def get_dict(self):
        return {
                "lat" : self.latitude,
                "lon" : self.longitude
                }
    
    def get_location(self):
        return Point(self.longitude, self.latitude)

    def __unicode__(self):
        return str(self.id)
