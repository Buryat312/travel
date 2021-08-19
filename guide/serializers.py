from rest_framework import serializers
from .models import Travel

class TravelSerializer(serializers.ModelSerializer):
    
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
 
    class Meta:
        model = Travel
        fields = ['country_name', 'body', 'img', 'created_at']