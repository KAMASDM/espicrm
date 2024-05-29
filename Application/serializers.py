from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        
    def validate(self, data):
        if 'application' not in data or data['application'] is None:
            data['application'] = None  # Ensure it is set to None if not provided
        return data

