from rest_framework.serializers import ModelSerializer
from .models import BusinessProfile, Comment, UserProfile, Category
from django.contrib.auth.models import User


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['first_name']:
            representation.pop('first_name')
        return representation


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'


class BusinessProfileSerializer(ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = BusinessProfile
        fields = ['user', 'category', 'title', 'description']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
