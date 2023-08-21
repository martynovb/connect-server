from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api import BusinessProfileViewSet

router = routers.DefaultRouter()
router.register('businesses', BusinessProfileViewSet, 'businesses')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('accounts.urls')),
]