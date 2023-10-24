from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import BasicForm
from .serializers import  BasicFormSerializer
from users.models import UserProfile

class BasicFormList(APIView):
    def get(self, request, format=None):
        basic_forms = BasicForm.objects.all()
        serializer = BasicFormSerializer(basic_forms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BasicFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BasicFormDetail(APIView):
    def get_object(self, pk):
        try:
            return BasicForm.objects.get(pk=pk)
        except BasicForm.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        basic_form = self.get_object(pk)
        serializer = BasicFormSerializer(basic_form)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        basic_form = self.get_object(pk)
        serializer = BasicFormSerializer(basic_form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        basic_form = self.get_object(pk)
        basic_form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def basic_form_list(request):
    basic_forms = BasicForm.objects.all()
    serializer = BasicFormSerializer(basic_forms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_user_to_shared_users(request, form_id, user_id):
        basic_form = BasicForm.objects.get(pk=form_id)
        user = UserProfile.objects.get(pk=user_id)
        basic_form.shared_users.add(user) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)