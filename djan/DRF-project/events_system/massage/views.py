from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from  .models import ChatMassage, Chat
from .serializers import ChatMassageSerializer, ChatSerializer
from rest_framework import viewsets

class ChatMassageViewSet(viewsets.ModelViewSet):
    queryset = ChatMassage.objects.all()
    serializer_class = ChatMassageSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
