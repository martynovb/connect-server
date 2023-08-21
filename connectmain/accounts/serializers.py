from abc import ABC

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from api.models import Category, BusinessProfile, UserProfile


# Registration

class BusinessRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    title = serializers.CharField()
    description = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        fields = ('email', 'title', 'description', 'category', 'password')

    def create(self, validated_data):
        print(validated_data)

        # Handle the User creation
        user = User(
            username=validated_data['email'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        # Handle the BusinessProfile creation
        business_profile = BusinessProfile.objects.create(
            user=user,
            title=validated_data['title'],
            description=validated_data['description'],
            category=validated_data['category']
        )
        return business_profile


class UserRegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        fields = ['full_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['full_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        user_profile = UserProfile.objects.create(user=user)

        return user_profile


# Login
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if user and user.is_active:
            try:
                user_profile = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                raise serializers.ValidationError(
                    "No user_type(user) with this email",
                    code="not_found")

            return user_profile
        raise serializers.ValidationError('Incorrect credentials',
                                          code="invalid_data")


class BusinessLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if user and user.is_active:
            try:
                business_profile = BusinessProfile.objects.get(user=user)
            except BusinessProfile.DoesNotExist:
                raise serializers.ValidationError(
                    "No user_type(business) with this email",
                    code="not_found")

            return business_profile
        raise serializers.ValidationError('Incorrect credentials',
                                          code="invalid_data")
