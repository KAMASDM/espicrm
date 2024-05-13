from rest_framework import viewsets,status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import enquiry
from .serializers import EnquirySerializer, EnquiryCreateSerializerss
from rest_framework.permissions import IsAuthenticated  
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.mail import send_mail
from django.conf import settings
import requests
class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = enquiry.objects.all()
    serializer_class = EnquirySerializer
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated] 
 
 
class EnquiryCreateView(generics.ListCreateAPIView):
    queryset = enquiry.objects.all()
    serializer_class = EnquiryCreateSerializerss   

    
    
    def create(self, request, *args, **kwargs):
            # Extract student_email from request data
            student_email = request.data.get('student_email', None)
            student_phone = request.data.get('student_phone',None)
            print(student_email)
            if not student_email:
                return Response({'error': 'student_email is required'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                # Send email
                self.send_enquiry_confirmation_email(serializer.instance, student_email)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_enquiry_confirmation_email(self, enquiry_instance, student_email):
        subject = 'Enquiry Confirmation'

            # Construct email content
        message = f"Thank you for submitting your enquiry with us!\n\n"
        message += f"We have received your enquiry details. Our team will get in touch with you shortly.\n\n"
        message += f"Enquiry Details:\n"
        message += f"First Name: {enquiry_instance.student_First_Name}\n"
        message += f"Last Name: {enquiry_instance.student_Last_Name}\n"
        message += f"Passport: {enquiry_instance.student_passport}\n"
        message += f"Phone: {enquiry_instance.student_phone}\n"
        message += f"Alternate Phone: {enquiry_instance.alternate_phone}\n"
        message += f"Address: {enquiry_instance.student_address}\n"
        message += f"Country: {enquiry_instance.student_country}\n"
        message += f"State: {enquiry_instance.student_state}\n"
        message += f"City: {enquiry_instance.student_city}\n"
        message += f"ZIP: {enquiry_instance.student_zip}\n"
        message += f"Current Education: {enquiry_instance.current_education}\n"
        message += f"Country Interested: {enquiry_instance.country_interested}\n"
        message += f"University Interested: {enquiry_instance.university_interested}\n"
        message += f"Course Interested: {enquiry_instance.course_interested}\n"
        message += f"Level Applying For: {enquiry_instance.level_applying_for}\n"
        message += f"Intake Interested: {enquiry_instance.intake_interested}\n"
        message += f"Assigned Users: {enquiry_instance.assigned_users}\n"
        message += f"Enquiry Status: {enquiry_instance.enquiry_status}\n"
        message += f"Notes: {enquiry_instance.notes}\n"
        message += f"Created By: {enquiry_instance.created_by}\n"
                # Send email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [student_email])
        
        
    def send_whatsapp_message(self,enquiry_instance,student_phone,student_First_Name):
        api_key = "634b7217-d8f7-11ed-a7c7-9606c7e32d76"
        sender_whatsapp_number = "917211117272"
        recipient_whatsapp_number = [student_phone]  # Assuming student_phone contains the WhatsApp number
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
                "url": "https://whatsappdata.s3.ap-south-1.amazonaws.com/userMedia/831c2f88a604a07ca94314b56a4921b8/testing_image.jpeg",
                "placeholders": [[student_First_Name], whatsapp_message],
                "buttons": [{
                    "index": 0,
                    "type": "visit_website",
                    "placeholder": "visitors-visa"
                }]
            }
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print("WhatsApp message sent successfully")
        else:
            print("Failed to send WhatsApp message")
        

    
    