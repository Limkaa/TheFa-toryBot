from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404

from .serializers import UserSerializer

from .models import User


class CreateUserAPI(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class MyProfileAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)