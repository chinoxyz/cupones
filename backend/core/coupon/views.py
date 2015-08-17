__author__ = 'josegregorio'

from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from rest_framework.views import APIView

from .models import BaseCoupon
from .forms import CouponForm


def all_coupons(request):
    coupons = BaseCoupon.objects.all()
    coupons_list = [coupon for coupon in coupons]
    context = {"couponlist": coupons_list}
    return render(request, 'coupon/couponlist.html', context)


class Coupon(APIView):
    follow = '/coupon'

    def get(self, request):
        context = {'form': CouponForm()}
        return render(request, 'coupon/create.html', context)

    def post(self, request):
        form = CouponForm(request.data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.follow)

        context = {'form': form}
        return render(request, 'coupon/create.html', context)
