__author__ = 'josegregorio'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_coupons, name='list_coupons'),
    url(r'^create$', views.Coupon.as_view(), name='create_coupon'),
    # url(r'^(?P<campaign_id>\d+)/$', views.detail, name='coupon_detail'), Soon
]