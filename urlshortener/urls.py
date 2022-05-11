from django.urls import path, re_path

from . import views

# app_name = 'urlshortener'
urlpatterns = [
    path('', views.index, name='home'),
    path('new_short_url/<str:surl>/', views.new_short_url, name='new_short_url'),
    #path('new_short_url/(?P<surl>[^/]+)/', views.new_short_url, name='new_short_url'),
    path('<str:surl>/', views.shorten, name='shorten'),
    # path('<str:surl>/stats', views.statistic, name='stats'),
    # re_path(r'^(?P<surl>)/$', views.shorten, name='shorten'),
]
