from django.contrib import admin
from django.urls import path, include
from .views import link_to_fragment, month_user
urlpatterns = [

    path('links/', link_to_fragment, name='link_to_fragment'),
    path('user_month/', month_user, name='month_user')
]
