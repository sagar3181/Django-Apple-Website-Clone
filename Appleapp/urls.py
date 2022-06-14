from django.urls import path
from . import views
urlpatterns={
    path('home',views.home,name="index"),
    path('iphone',views.iphone,name="iphone"),
    path('mac',views.mac,name="mac"),
    path('ipad',views.ipad,name="ipad"),
    path('watch',views.watch,name="watch"),
    path('tv',views.tv,name="tv"),
    path('music',views.music,name="music"),
    path('accessories',views.accessories,name="accessories"), 
    path('service',views.service,name="service"),
    path('error',views.error,name="error"),
    path('applestore',views.applestore,name="applestore"),
    path('appleeducation',views.appleeducation,name="appleeducation"),
    path('account',views.account,name="account"),
    path('accounterror',views.accounterror,name="accounterror"),
    path('accessibility',views.accessibility,name="accessibility"),
    path('environment',views.environment,name="environment"),
    path('iphone12',views.iphone12,name="iphone12"),
    path('iphone12pro',views.iphone12pro,name="iphone12pro"),
    path('ipadair',views.ipadair,name="ipadair"),
    path('ipadpro',views.ipadpro,name="ipadpro"),
    path('macbookair',views.macbookair,name="macbookair"),
    path('macbookpro',views.macbookpro,name="macbookpro")

}