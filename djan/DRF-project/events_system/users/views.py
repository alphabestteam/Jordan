from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import UserProfile
from massage.models import ChatMassage
from .serializers import UserProfileSerializer
from rest_framework import viewsets

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


@api_view(['POST'])
def add_unread_message_to_user(request, id_number, message_id):
    user = get_object_or_404(UserProfile, pk =id_number)
    message = get_object_or_404(ChatMassage, pk =message_id)
    if request.method == "POST":
        user.add_unread_message(message)
        return Response({"message": "Message added to unread_messages"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def mark_message_as_read(request, id_number, message_id):
    user = get_object_or_404(UserProfile,  pk =id_number)
    message = get_object_or_404(ChatMassage, pk=message_id)

    if request.method == "POST":
        user.mark_message_as_read(message)
        return Response({"message": "Message marked as read"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)

