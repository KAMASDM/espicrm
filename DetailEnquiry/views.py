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
from django.shortcuts import get_object_or_404
from Master.models import * 
from Enquiry.models import enquiry
class DetailEnquiryViewSet(viewsets.ModelViewSet):
    queryset = Detail_Enquiry.objects.all()
    serializer_class = DetailEnquirySerializer
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]
    
    # def create(self, request, *args, **kwargs):
    #     # Validate Current_Enquiry
    #     current_enquiry_id = Detail_Enquiry.objects.get('Current_Enquiry')
    #     if current_enquiry_id is not None:
    #         current_enquiry = enquiry.objects.get(id=current_enquiry_id)
            
    #     current_enquiry_data = {
    #                 'id': current_enquiry.id,
    #                 'student_First_Name': current_enquiry.student_First_Name,
    #                 'student_Last_Name': current_enquiry.student_Last_Name,
    #                 'student_passport': current_enquiry.student_passport,
    #                 'student_phone': current_enquiry.student_phone,
    #                 # 'alternate_phone': current_enquiry.alternate_phone,
    #                 # 'student_address': current_enquiry.student_address,
    #                 # 'student_country': current_enquiry.student_country,
    #                 # 'student_state': current_enquiry.student_state,
    #                 # 'student_city': current_enquiry.student_city,
    #                 # 'student_zip': current_enquiry.student_zip,
    #                 # 'current_education': current_enquiry.current_education,
    #                 # 'country_interested': current_enquiry.country_interested,
    #                 # 'university_interested': current_enquiry.university_interested,
    #                 # 'course_interested': current_enquiry.course_interested,
    #                 # 'level_applying_for': current_enquiry.level_applying_for,
    #                 # 'intake_interested': current_enquiry.intake_interested,
    #                 # 'assigned_users': current_enquiry.assigned_users,
    #                 # Add other fields as needed
    #             }

        
    #     current_enquiry_id = request.data.get('current_enquiry_data')
    
    #     current_enquiry = get_object_or_404(enquiry, id=current_enquiry_id)
     

    #     request.data['Current_Enquiry'] = current_enquiry
       

    #     serializer = DetailEnquirySerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def send_enquiry_confirmation_email(self, enquiry_instance, student_email):
        subject = 'Enquiry Confirmation'
        related_enquiry = enquiry_instance.Current_Enquiry

    # Extract student_email from the related enquiry instance
        student_email = related_enquiry.student_email

        # Construct email content
        message = f"Thank you for submitting your Deatil enquiry with us!\n\n"
        message += f"We have received your Deatil enquiry details. Our team will get in touch with you shortly.\n\n"
        message += f"Deatil Enquiry Details:\n"
        message += f"Current Enquiry: {enquiry_instance.Current_Enquiry}\n"
        message += f"Current Education Details: {enquiry_instance.Current_Education_Details}\n"
        message += f"Tenth Education Details: {enquiry_instance.Tenth_Education_Details}\n"
        message += f"Twelveth Education Details: {enquiry_instance.Twelveth_Education_Details}\n"
        message += f"Graduation Education Details: {enquiry_instance.Graduation_Education_Details}\n"
        message += f"Work Experience: {enquiry_instance.Work_Experience}\n"
        message += f"Toefl Exam: {enquiry_instance.Toefl_Exam}\n"
        message += f"Ielts Exam: {enquiry_instance.ielts_Exam}\n"
        message += f"PTE Exam: {enquiry_instance.PTE_Exam}\n"
        message += f"Duolingo Exam: {enquiry_instance.Duolingo_Exam}\n"
        message += f"Gre Exam: {enquiry_instance.Gre_Exam}\n"
        message += f"Gmat Exam: {enquiry_instance.Gmat_Exam}\n"
        message += f"Father's Occupation: {enquiry_instance.Father_Occupation}\n"
        message += f"Father's Annual Income: {enquiry_instance.Father_Annual_Income}\n"
        message += f"Refusal: {enquiry_instance.Refusal}\n"
        message += f"Twelveth Document: {enquiry_instance.Twelveth_Document}\n"
        message += f"Tenth Document: {enquiry_instance.Tenth_Document}\n"
        message += f"Graduation Marksheet: {enquiry_instance.Graduation_Marksheet}\n"
        message += f"Graduation Certificate: {enquiry_instance.Graduation_Certificate}\n"
        message += f"UG Marksheet: {enquiry_instance.UG_Marksheet}\n"
        message += f"UG Certificate: {enquiry_instance.UG_Certificate}\n"
        message += f"Work Experience Document: {enquiry_instance.Work_Experience_Document}\n"
        message += f"Passport Document: {enquiry_instance.Passport_Document}\n"
        message += f"Offer Letter: {enquiry_instance.Offer_Letter}\n"
        message += f"IELTS Result: {enquiry_instance.Ielts_Result}\n"
        message += f"Toefl Result: {enquiry_instance.Toefl_Result}\n"
        message += f"PTE Result: {enquiry_instance.PTE_Result}\n"
        message += f"Duolingo Result: {enquiry_instance.Duolingo_Result}\n"
        message += f"GRE Result: {enquiry_instance.Gre_Result}\n"
        message += f"GMAT Result: {enquiry_instance.Gmat_Result}\n"
        message += f"Confirmed Services: {', '.join(str(service) for service in enquiry_instance.Confirmed_Services.all())}\n"
        message += f"Detail Enquiry Followup: {enquiry_instance.DetaiEnquiryFollowup}\n"
        message += f"Enquiry Status: {enquiry_instance.Enquiry_Status}\n"
        # Include other fields as needed





        # Send email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [student_email])


class DetailEnquiryCreate(generics.ListCreateAPIView):
    queryset = Detail_Enquiry.objects.all()
    serializer_class = DetailEnquirySerializer

    
    
    
    


    

    
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
