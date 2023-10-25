from rest_framework import serializers
from .models import FileForm

class FileFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileForm
        fields = '__all__'