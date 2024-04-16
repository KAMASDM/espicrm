from rest_framework import viewsets
from .models import enquiry
from .serializers import EnquirySerializer
from rest_framework.response import Response
import requests

from django.db.models.signals import post_save
from django.dispatch import receiver
from Enquiry.models import enquiry

# Import the necessary modules for sending notifications
import requests

class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = enquiry.objects.all()
    serializer_class = EnquirySerializer
    
    def perform_create(self, serializer):
        instance = serializer.save()
        print(instance)
        self.send_notifications(instance)
        return Response(serializer.data)

    def send_notifications(self, instance):
        # Send WhatsApp message
        api_key = "634b7217-d8f7-11ed-a7c7-9606c7e32d76"
        sender_whatsapp_number = "917211117272"
        recipient_whatsapp_number = instance.student_phone
        whatsapp_message = "Hello, your enquiry has been submitted successfully. We will get back to you soon."
            
        url = "https://wapi.flexiwaba.com/v1/wamessage/sendMessage"
        headers = {
                "Content-Type": "application/json",
                "apiKey": api_key
            }
        payload = {
                "from": sender_whatsapp_number,
                "to": recipient_whatsapp_number,
                "type": "template",
                "message": {
            "templateid": "195283",
            "image": "https://whatsappdata.s3.ap-south-1.amazonaws.com/userMedia/831c2f88a604a07ca94314b56a4921b8/testing_image.jpeg",
            "placeholders": ["Ramesh", "Visa Service",whatsapp_message],
            "buttons": [{
                "index": 0,
                "type": "visit_website",
                "placeholder":"visitors-visa"
            }]
        }
        }
        response = requests.post(url, json=payload, headers=headers)
        print(response)
        if response.status_code == 200:
            print("WhatsApp message sent successfully")
        else:
                print("Failed to send WhatsApp message")


    # @receiver(post_save, sender=enquiry)
    # def send_whatsapp_notification(sender, instance, created, **kwargs):
    #     if created:
    #         # Send WhatsApp message logic
    #         api_key = "634b7217-d8f7-11ed-a7c7-9606c7e32d76"
    #         sender_whatsapp_number = "917211117272"
    #         recipient_whatsapp_number = instance.student_phone
    #         whatsapp_message = "Hello, your enquiry has been submitted successfully. We will get back to you soon."
                
    #         url = "https://wapi.flexiwaba.com/v1/wamessage/sendMessage"
    #         headers = {
    #             "Content-Type": "application/json",
    #             "apiKey": api_key
    #         }
    #         payload = {
    #             "from": sender_whatsapp_number,
    #             "to": recipient_whatsapp_number,
    #             "type": "template",
    #             "message": {
    #                 "templateid": "195283",
    #                 "url": "https://whatsappdata.s3.ap-south-1.amazonaws.com/userMedia/831c2f88a604a07ca94314b56a4921b8/testing_image.jpeg",
    #                 "placeholders": ["Ramesh", "Visa Service"],
    #                 "buttons": [{
    #                     "index": 0,
    #                     "type": "visit_website",
    #                     "placeholder": "Visit Website"
    #                 }]
    #             }
    #         }
    #         response = requests.post(url, json=payload, headers=headers)
    #         if response.status_code == 200:
    #             print("WhatsApp message sent successfully")
    #         else:
    #             print("Failed to send WhatsApp message")
