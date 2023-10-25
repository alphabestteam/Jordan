from rest_framework import serializers
from .models import ChatMassage, Chat

class ChatMassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMassage
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'