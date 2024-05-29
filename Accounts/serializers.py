from rest_framework import serializers
from .models import Payment
from DetailEnquiry.serializers import *
from DetailEnquiry.models import *
from Master.models import *
# class PaymentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payment
#         fields = '__all__'
#         depth = 2

class PaymentSerializer(serializers.ModelSerializer):
    Memo_For_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    payment_mode = serializers.IntegerField(write_only=True, required=True)  # Ensure this is required
    payment_received_by = serializers.IntegerField(write_only=True, required=True)  # Ensure this is required

    class Meta:
        model = Payment
        fields = '__all__'
    
    def create(self, validated_data):
        memo_for_id = validated_data.pop('Memo_For_id', None)
        if memo_for_id:
            memo_for = Detail_Enquiry.objects.get(id=memo_for_id)
            validated_data['Memo_For'] = memo_for

        payment_mode = validated_data.pop('payment_mode')
        payment_mode = Payment_Mode.objects.get(id=payment_mode)
        validated_data['payment_mode'] = payment_mode

        payment_received_by = validated_data.pop('payment_received_by')
        payment_received_by = get_user_model().objects.get(id=payment_received_by)
        validated_data['payment_received_by'] = payment_received_by

        return super().create(validated_data)