from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api import BusinessProfileViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register('businesses', BusinessProfileViewSet, 'businesses')
router.register('reviews', ReviewViewSet, 'reviews')

urlpatterns = [
    path('reviews/business/<int:business_profile_id>/', ReviewViewSet.as_view({'get': 'list_by_business'})),
    path('', include(router.urls)),
    path('', include('accounts.urls')),
]