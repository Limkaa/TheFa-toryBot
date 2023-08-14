from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import MessageSerializer
from .models import Message

from ..bot_tokens.models import UserBotToken


class ListCreateMessageAPI(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer, token):
        return serializer.save(user=self.request.user, token=token)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        token = UserBotToken.objects.filter(user=self.request.user).first()
        if not token:
            return Response({"detail": "Сначала сгенерируйте токен для бота!"}, status=status.HTTP_400_BAD_REQUEST) 
        elif not token.chat_id:
            return Response({"detail": "Теперь отправьте токен боту, чтобы подключить чат!"}, status=status.HTTP_400_BAD_REQUEST) 
        
        self.perform_create(serializer, token)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def filter_queryset(self, queryset):
        return self.queryset.filter(user=self.request.user)