__author__ = 'josegregorio'

from django.conf.urls import url

from . import views
from backend.core.coupon.views import CouponListView

urlpatterns = [
    url(r'^$', CouponListView.as_view(), name='index'),
    # url(r'^(?P<campaign_id>\d+)/$', views.detail, name='coupon_detail'), Soon
]