from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Detail_Enquiry
from .serializers import DetailEnquirySerializer
from rest_framework.response import Response
import requests
class DetailEnquiryViewSet(viewsets.ModelViewSet):
    queryset = Detail_Enquiry.objects.all()
    serializer_class = DetailEnquirySerializer
    
    
    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_notifications(instance)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        self.send_deletion_notification(instance)
        instance.delete()

    def send_notifications(self, instance):
        # Send WhatsApp message
        api_key = "634b7217-d8f7-11ed-a7c7-9606c7e32d76"
        sender_whatsapp_number = "917211117272"
        recipient_whatsapp_number = instance.student_phone
        whatsapp_message = "Hello, your Detail enquiry has been submitted successfully. We will get back to you soon."
        
        url = "https://wapi.flexiwaba.com/v1/wamessage/sendMessage"
        headers = {
            "Content-Type": "application/json",
            "apiKey": api_key
        }
        payload = {
            "from": sender_whatsapp_number,
            "to": recipient_whatsapp_number,
            "type": "text",
            "message": {
                "text": whatsapp_message
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print("WhatsApp message sent successfully")
        else:
            print("Failed to send WhatsApp message")
