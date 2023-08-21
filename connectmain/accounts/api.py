from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserRegisterSerializer, BusinessRegisterSerializer, \
    UserLoginSerializer, BusinessLoginSerializer
from api.serializers import BusinessProfileSerializer, UserProfileSerializer

from api.models import BusinessProfile, UserProfile


class UserRegisterAPI(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_profile = serializer.save()
        user = user_profile.user

        return Response({
            "data": UserProfileSerializer(user_profile, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class BusinessRegisterAPI(generics.GenericAPIView):
    serializer_class = BusinessRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        business_profile = serializer.save()

        user = business_profile.user

        return Response({
            "data": BusinessProfileSerializer(business_profile, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserLoginAPI(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_profile = serializer.validated_data

        user = user_profile.user

        return Response({
            "data": UserProfileSerializer(user_profile, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class BusinessLoginAPI(generics.GenericAPIView):
    serializer_class = BusinessLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        business_profile = serializer.validated_data

        user = business_profile.user

        return Response({
            "data": BusinessProfileSerializer(business_profile, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class BusinessProfileAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = BusinessLoginSerializer

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        business_profile = BusinessProfile.objects.get(user=user)
        return Response({
            "data": BusinessProfileSerializer(business_profile, context=self.get_serializer_context()).data,
        })


class UserProfileAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        user_profile = UserProfile.objects.get(user=user)
        return Response({
            "data": UserProfileSerializer(user_profile, context=self.get_serializer_context()).data,
        })
