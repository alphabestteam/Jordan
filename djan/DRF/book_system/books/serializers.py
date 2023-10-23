from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    custom_field = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'title','author' ,'genre', 'description')
        #READ ONLY FIELD
        read_only_fields = ('publication_year')
    
    # CREATING EXTRA FIELD
    def get_custom_field(self, obj):
        return f"Custom Value for {obj.title}"
