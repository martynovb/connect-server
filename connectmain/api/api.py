from rest_framework.response import Response
from rest_framework.decorators import action

from .models import BusinessProfile, Review
from rest_framework import viewsets, permissions, status
from .serializers import BusinessProfileSerializer, ReviewSerializer
from .permissions.is_owner_or_read_only import IsOwnerOrReadOnly
from rest_framework import serializers


class BusinessProfileViewSet(viewsets.ModelViewSet):
    queryset = BusinessProfile.objects.all()
    permission_classes = [
        # permissions.IsAuthenticated,
        # IsOwnerOrReadOnly
    ]
    serializer_class = BusinessProfileSerializer


# def get_queryset(self):
#    return BusinessProfile.objects.filter(user=self.request.user)

# def perform_create(self, serializer):
#    serializer.save(user=self.request.user)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    ]
    serializer_class = ReviewSerializer

    @action(detail=False, methods=['GET'])
    def list_by_business(self, request, business_profile_id=None):
        queryset = Review.objects.filter(businessProfile__id=business_profile_id)
        serializer = ReviewSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save(user=None)

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'detail': 'User is not authenticated'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
