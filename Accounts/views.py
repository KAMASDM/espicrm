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
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = [JWTAuthentication]      
    permission_classes = [IsAuthenticated]
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            # Send email
            self.send_payment_confirmation_email(serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_payment_confirmation_email(self, payment_instance):
        subject = 'Payment Confirmation'
        recipient_email = 'recipient@example.com'  # Change to actual recipient email address

        # Construct email content
        message = f"Thank you for submitting! Below are the details of your payment:\n\n"
        message += f"Payment ID: {payment_instance.payment_id}\n"
        message += f"Payment Type: {payment_instance.Payment_Type}\n"
        message += f"Payment Date: {payment_instance.payment_date}\n"
        message += f"Payment Amount: {payment_instance.payment_amount}\n"
        message += f"Payment Mode: {payment_instance.payment_mode}\n"
        message += f"Payment Status: {payment_instance.payment_status}\n"
        message += f"Payment Reference: {payment_instance.payment_reference}\n"
        message += f"Payment Remarks: {payment_instance.payment_remarks}\n"
        message += f"Received By: {payment_instance.payment_received_by}\n"
        # Add more fields as needed
        message += f"Memo For: {payment_instance.Memo_For}\n"
        message += f"Payment Followup: {payment_instance.PaymentFollowup}\n"

        # Send email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])