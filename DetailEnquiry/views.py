from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,status
from .models import Detail_Enquiry
from .serializers import DetailEnquirySerializer
from rest_framework.response import Response
import requests
from rest_framework.permissions import IsAuthenticated  
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings
class DetailEnquiryViewSet(viewsets.ModelViewSet):
    queryset = Detail_Enquiry.objects.all()
    serializer_class = DetailEnquirySerializer
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]

class DetailEnquiryCreate(generics.ListCreateAPIView):
    queryset = Detail_Enquiry.objects.all()
    serializer_class = DetailEnquirySerializer
    


def send_enquiry_confirmation_email(self, enquiry_instance):
    subject = 'Detail Enquiry Confirmation'

    message = f"Thank you for submitting your detail enquiry with us!\n\n"
    message += f"We have received your detail enquiry details. Our team will get in touch with you shortly.\n\n"
    message += f"Enquiry Details:\n"
    message += f"First Name: {enquiry_instance.Current_Enquiry.student_First_Name}\n"
    message += f"Last Name: {enquiry_instance.Current_Enquiry.student_Last_Name}\n"
    message += f"Passport: {enquiry_instance.Current_Enquiry.student_passport}\n"
    message += f"Phone: {enquiry_instance.Current_Enquiry.student_phone}\n"
    message += f"Alternate Phone: {enquiry_instance.Current_Enquiry.alternate_phone}\n"
    message += f"Address: {enquiry_instance.Current_Enquiry.student_address}\n"
    message += f"Country: {enquiry_instance.Current_Enquiry.student_country}\n"
    message += f"State: {enquiry_instance.Current_Enquiry.student_state}\n"
    message += f"City: {enquiry_instance.Current_Enquiry.student_city}\n"
    message += f"ZIP: {enquiry_instance.Current_Enquiry.student_zip}\n"
    message += f"Current Education: {enquiry_instance.Current_Education_Details}\n"
    message += f"Work Experience: {enquiry_instance.Work_Experience}\n"
    # Add more fields as needed

    send_mail(subject, message, settings.EMAIL_HOST_USER, [enquiry_instance.Current_Enquiry.student_email])

    # Log email sent if needed
    print("Detail enquiry confirmation email sent successfully to:", enquiry_instance.Current_Enquiry.student_email)

    

    
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     self.send_notifications(instance)
    #     return Response(serializer.data)

    # def perform_destroy(self, instance):
    #     self.send_deletion_notification(instance)
    #     instance.delete()

    # def send_notifications(self, instance):
    #     # Send WhatsApp message
    #     api_key = "634b7217-d8f7-11ed-a7c7-9606c7e32d76"
    #     sender_whatsapp_number = "917211117272"
    #     recipient_whatsapp_number = instance.enstudent_phone
    #     whatsapp_message = "Hello, your Detail enquiry has been submitted successfully. We will get back to you soon."
        
    #     url = "https://wapi.flexiwaba.com/v1/wamessage/sendMessage"
    #     headers = {
    #         "Content-Type": "application/json",
    #         "apiKey": api_key
    #     }
    #     payload = {
    #         "from": sender_whatsapp_number,
    #         "to": recipient_whatsapp_number,
    #         "type": "text",
    #         "message": {
    #             "text": whatsapp_message
    #         }
    #     }
    #     response = requests.post(url, json=payload, headers=headers)
    #     if response.status_code == 200:
    #         print("WhatsApp message sent successfully")
    #     else:
    #         print("Failed to send WhatsApp message")
