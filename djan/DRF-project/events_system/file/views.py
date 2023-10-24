from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FileForm
from .serializers import FileFormSerializer
from django.shortcuts import get_object_or_404


class FileCreateView(APIView):
    def post(self, request):
        serializer = FileFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
