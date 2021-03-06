from django.urls import path, re_path

from . import views

# app_name = 'urlshortener'
urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('stats/', views.statistic, name='stats'),
    # path('new_short_url/', views.new_short_url, name='new_short_url'),
    path('<str:surl>/', views.shorten, name='shorten'),

]
