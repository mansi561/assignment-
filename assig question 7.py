from rest_framework.permissions import BasePermission
class IsProUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.license_type == 'pro'
    



    from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProUser
from .serializers import ImageSerializer


class ImageUploadView(generics.CreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated, IsProUser]