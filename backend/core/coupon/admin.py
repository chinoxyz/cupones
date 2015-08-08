__author__ = 'josegregorio'

from django.contrib import admin
from .models import BaseCoupon, Coupon

admin.site.register(BaseCoupon)
admin.site.register(Coupon)
