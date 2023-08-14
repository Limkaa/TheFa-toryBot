from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .serializers import UserBotTokenSerializer
from .models import UserBotToken


class UserTokenAPI(generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = UserBotToken.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserBotTokenSerializer
    
    def get_object(self):
        return get_object_or_404(self.queryset, user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    