__author__ = 'josegregorio'

from django.forms.models import ModelForm
from django.db import transaction

from .models import BaseCoupon


class CouponForm(ModelForm):

    class Meta:
        model = BaseCoupon
        fields = ['title', 'price', 'details', 'conditions', 'information', 'expiration_date']

    error_css_class = 'error'

    @transaction.atomic
    def save(self, *args, **kwargs):
        data = self.cleaned_data
        coupon = BaseCoupon(title=data.get("title"),
                            price=data.get("price"),
                            details=data.get("details"),
                            conditions=data.get("conditions"),
                            information=data.get("information"),
                            expiration_date=data.get("expiration_date"))

        coupon.save()

        return coupon
