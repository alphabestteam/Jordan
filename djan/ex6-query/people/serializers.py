from .models import Person, Parent
from rest_framework import serializers

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person 
        fields = ['id_number', 'name', 'birth_date', 'city']
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'