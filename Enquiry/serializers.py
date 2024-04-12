from rest_framework import serializers
from .models import enquiry
from django.contrib.auth import get_user_model

# Import models from other apps if needed

class EnquirySerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    country_interested = serializers.CharField(source='country_interested.country')
   
      # Assuming your Country model has a 'name' field.

    # ... Do the same for other ForeignKey fields ...

    class Meta:
        model = enquiry
        fields = '__all__'
        depth = 2


class EnquiryCreateSerializerss(serializers.ModelSerializer):
    class Meta:
        model = enquiry
        fields = '__all__'
