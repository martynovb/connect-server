from django.urls import path, include
from .api import BusinessRegisterAPI, UserRegisterAPI, UserLoginAPI, \
    BusinessLoginAPI, BusinessProfileAPI, UserProfileAPI
from knox import views as knox_views

urlpatterns = [
    path('auth', include('knox.urls')),

    path('auth/register/user', UserRegisterAPI.as_view(), name='business-register'),
    path('auth/register/business', BusinessRegisterAPI.as_view(), name='user-register'),

    path('auth/login/user', UserLoginAPI.as_view(), name='user-login'),
    path('auth/login/business', BusinessLoginAPI.as_view(), name='business-login'),

    path('auth/profile/user', UserProfileAPI.as_view(), name='user-profile'),
    path('auth/profile/business', BusinessProfileAPI.as_view(), name='business-profile'),

    path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
]
