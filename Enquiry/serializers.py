from rest_framework import serializers
from .models import enquiry
from django.contrib.auth import get_user_model

# Import models from other apps if needed

class EnquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = enquiry
        fields = '__all__'
        depth = 2


class EnquiryCreateSerializerss(serializers.ModelSerializer):
    class Meta:
        model = enquiry
        fields = '__all__'
