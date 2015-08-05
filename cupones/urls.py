from django.conf.urls import patterns, include, url
from django.contrib import admin

from backend.core.coupon.views import CouponListView


urlpatterns = patterns('',
    url(r'^$', CouponListView.as_view()),
    url(r'^coupon/', include('backend.core.coupon.urls')),
    url(r'^admin/', include(admin.site.urls)),
)