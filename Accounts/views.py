from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework.permissions import IsAuthenticated  
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from DetailEnquiry.models import Detail_Enquiry
from django.contrib.auth import get_user_model
from Master.models import * 
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = [JWTAuthentication]      
    permission_classes = [IsAuthenticated]
    
    
def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        memo_for_id = request.data.get('Memo_For_id')
        if memo_for_id:
            try:
                memo_for = Detail_Enquiry.objects.get(id=memo_for_id)
                serializer.validated_data['Memo_For'] = memo_for
            except Detail_Enquiry.DoesNotExist:
                return Response({"error": "Detail_Enquiry with this ID does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        payment_mode_id = request.data.get('payment_mode_id')
        if not payment_mode_id:
            return Response({"error": "payment_mode_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            payment_mode = Payment_Mode.objects.get(id=payment_mode_id)
            serializer.validated_data['payment_mode'] = payment_mode
        except Payment_Mode.DoesNotExist:
            return Response({"error": "Payment_Mode with this ID does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        payment_received_by = request.data.get('payment_received_by')
        if not payment_received_by:
            return Response({"error": "payment_received_by_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            payment_received_by = get_user_model().objects.get(id=payment_received_by)
            serializer.validated_data['payment_received_by'] = payment_received_by
        except get_user_model().DoesNotExist:
            return Response({"error": "User with this ID does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def send_payment_confirmation_email(self, payment_instance):
    #     subject = 'Payment Confirmation'
    #     recipient_email = 'recipient@example.com'  # Change to actual recipient email address

    #     # Construct email content
    #     message = f"Thank you for submitting! Below are the details of your payment:\n\n"
    #     message += f"Payment ID: {payment_instance.payment_id}\n"
    #     message += f"Payment Type: {payment_instance.Payment_Type}\n"
    #     message += f"Payment Date: {payment_instance.payment_date}\n"
    #     message += f"Payment Amount: {payment_instance.payment_amount}\n"
    #     message += f"Payment Mode: {payment_instance.payment_mode}\n"
    #     message += f"Payment Status: {payment_instance.payment_status}\n"
    #     message += f"Payment Reference: {payment_instance.payment_reference}\n"
    #     message += f"Payment Remarks: {payment_instance.payment_remarks}\n"
    #     message += f"Received By: {payment_instance.payment_received_by}\n"
    #     # Add more fields as needed
    #     message += f"Memo For: {payment_instance.Memo_For}\n"
    #     message += f"Payment Followup: {payment_instance.PaymentFollowup}\n"

    #     # Send email
    #     send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])