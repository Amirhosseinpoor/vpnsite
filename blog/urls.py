from django.contrib import admin
from django.urls import path, include
from .views import BlogView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
