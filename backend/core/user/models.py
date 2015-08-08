# Create your models here.



from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import OneToOneField, ForeignKey
from django.db.models.fields import CharField,EmailField, BooleanField


# class tokenPassword(models.Model):
#    user = OneToOneField(User)
#    token = CharField()


class AppUser(models.Model):
    user = OneToOneField(User)
    company = CharField(max_length=30, null=True, blank=True)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    initial_email = EmailField(null=True, blank=True)

    def change_password(self, password, newpassword):
        if self.user.check_password(password):
            self.user.set_password(newpassword)
            self.user.save()
            return True
        else:
            return False

    def __unicode__(self):
        return self.first_name + " " + self.last_name
