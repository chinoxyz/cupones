from django.conf.urls import patterns, include, url
from django.contrib import admin

from backend.core.coupon import views as coupons_views


urlpatterns = patterns('',
    url(r'^$', coupons_views.all_coupons, name="index"),
    url(r'^user/', include('backend.core.user.urls')),
    url(r'^coupon/', include('backend.core.coupon.urls')),
    url(r'^admin/', include(admin.site.urls)),
)