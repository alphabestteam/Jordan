from rest_framework import serializers
from .models import BasicForm

class BasicFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicForm
        fields = '__all__'



