from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import BasicForm
from .serializers import  BasicFormSerializer
from users.models import UserProfile
from rest_framework import viewsets

class BasicFormViewSet(viewsets.ModelViewSet):
    queryset = BasicForm.objects.all()
    serializer_class = BasicFormSerializer


