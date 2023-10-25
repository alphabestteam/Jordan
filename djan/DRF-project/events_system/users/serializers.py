
from rest_framework import serializers
from .models import UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [field.name for field in UserProfile._meta.fields if field.name != 'unread_messages']
        read_only_fields = ['unread_messages']