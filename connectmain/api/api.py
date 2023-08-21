from .models import BusinessProfile
from rest_framework import viewsets, permissions
from .serializers import BusinessProfileSerializer
from .permissions.is_owner_or_read_only import IsOwnerOrReadOnly


class BusinessProfileViewSet(viewsets.ModelViewSet):
    queryset = BusinessProfile.objects.all()
    permission_classes = [
        #permissions.IsAuthenticated,
        #IsOwnerOrReadOnly
    ]
    serializer_class = BusinessProfileSerializer

   # def get_queryset(self):
    #    return BusinessProfile.objects.filter(user=self.request.user)

    #def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)
