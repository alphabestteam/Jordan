from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FileForm
from .serializers import FileFormSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import viewsets
from users.models import UserProfile

class FileFormViewSet(viewsets.ModelViewSet):
    queryset = FileForm.objects.all()
    serializer_class = FileFormSerializer

@api_view(['POST'])
def add_user_to_shared_users(request, uploader, id_number):
        file_from = get_object_or_404(FileForm, uploader=uploader)
        user = get_object_or_404(UserProfile, id_number=id_number)  
        file_from.form.shared_users.add(user) 
        return Response({"message": "User added to shared users"}, status=status.HTTP_201_CREATED)