__author__ = 'josegregorio'

from django.shortcuts import render
from django.http import HttpResponse


def all_coupons(request):
    context = {"couponlist": [1]}
    return render(request, 'coupon/couponlist.html', context)
