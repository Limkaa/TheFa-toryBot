from rest_framework import serializers, exceptions

from .models import UserBotToken


class UserBotTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBotToken
        fields = ('id', 'user', 'token', 'chat_id', )
        read_only_fields = ('id', 'user', 'token', 'chat_id', )

    def create(self, validated_data):
        obj, created = UserBotToken.objects.get_or_create(user=validated_data['user'])
        
        # if created:
        #     obj.token = generate_token()
        #     obj.save()
            
        return obj