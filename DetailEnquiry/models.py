from django.db import models

# Create your models here.
from Enquiry.models import enquiry
from Master.models import (Edu_Level, Work_Experience, Toefl_Exam, Ielts_Exam, PTE_Exam,
                           Duolingo_Exam, Gre_Exam, Gmat_Exam, Rejection_Reason, Available_Services,Followup,Detail_Enquiry_Status)
from django.core.mail import EmailMessage
from django.conf import settings
import requests
class Detail_Enquiry(models.Model):

    Current_Enquiry = models.ForeignKey(enquiry, on_delete=models.CASCADE)
    Current_Education_Details = models.ForeignKey(Edu_Level, on_delete=models.CASCADE, blank=True, null=True)
    Tenth_Education_Details = models.ForeignKey(Edu_Level, on_delete=models.CASCADE, blank=True, null=True, related_name='Tenth_Education_Details')
    Twelveth_Education_Details = models.ForeignKey(Edu_Level, on_delete=models.CASCADE, blank=True, null=True, related_name='Twelveth_Education_Details')
    Graduation_Education_Details = models.ForeignKey(Edu_Level, on_delete=models.CASCADE, blank=True, null=True, related_name='Graduation_Education_Details')
    Work_Experience = models.ForeignKey(Work_Experience,max_length=100, on_delete=models.CASCADE, blank=True, null=True)
    Toefl_Exam = models.ForeignKey(Toefl_Exam, on_delete=models.CASCADE, blank=True, null=True)
    ielts_Exam = models.ForeignKey(Ielts_Exam, on_delete=models.CASCADE, blank=True, null=True)
    PTE_Exam = models.ForeignKey(PTE_Exam, on_delete=models.CASCADE, blank=True, null=True)
    Duolingo_Exam = models.ForeignKey(Duolingo_Exam, on_delete=models.CASCADE, blank=True, null=True)
    Gre_Exam = models.ForeignKey(Gre_Exam, on_delete=models.CASCADE, blank=True, null=True)
    Gmat_Exam = models.ForeignKey(Gmat_Exam, on_delete=models.CASCADE, blank=True, null=True)
    Father_Occupation = models.CharField(max_length=100, blank=True, null=True)
    Father_Annual_Income = models.FloatField(blank=True, null=True)
    Refusal = models.ForeignKey(Rejection_Reason, on_delete=models.CASCADE, blank=True, null=True)
    Twelveth_Document = models.FileField(upload_to='documents/', blank=True)
    Tenth_Document = models.FileField(upload_to='documents/', blank=True)
    Graduation_Marksheet = models.FileField(upload_to='documents/', blank=True)
    Graduation_Certificate = models.FileField(upload_to='documents/', blank=True)
    UG_Marksheet = models.FileField(upload_to='documents/', blank=True)
    UG_Certificate = models.FileField(upload_to='documents/', blank=True)
    Work_Experience_Document = models.FileField(upload_to='documents/', blank=True)
    Passport_Document = models.FileField(upload_to='documents/', blank=True)
    Offer_Letter = models.FileField(upload_to='documents/', blank=True)
    Ielts_Result = models.FileField(upload_to='documents/', blank=True)
    Toefl_Result = models.FileField(upload_to='documents/', blank=True)
    PTE_Result = models.FileField(upload_to='documents/', blank=True)
    Duolingo_Result = models.FileField(upload_to='documents/', blank=True)
    Gre_Result = models.FileField(upload_to='documents/', blank=True)
    Gmat_Result = models.FileField(upload_to='documents/', blank=True)
    Confirmed_Services = models.ManyToManyField(Available_Services, blank=True)
    followup = models.ForeignKey(Followup, on_delete=models.SET_NULL, null=True, blank=True)
    Enquiry_Status = models.ForeignKey(Detail_Enquiry_Status, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
            return (f"{self.Current_Enquiry}")
        
    def save(self, *args, **kwargs):
            # Call the original save method
        super().save(*args, **kwargs)
    
        # Send email to admin
        admin_subject = "New Detail Enquiry Submitted"
        admin_message = (
            f"A new Detail enquiry has been submitted with ID: {self.id}."
        )
        admin_email = settings.ADMIN_EMAIL
        admin_email_message = EmailMessage(admin_subject, admin_message, settings.DEFAULT_FROM_EMAIL, [admin_email])
        admin_email_message.send()
    
        # Send email to student
        student_subject = "Thank You for Your Detail Enquiry"
        student_message = (
            f"Thank you for your Detail Enquiry. We will get back to you shortly."
    
    
        )
        for field in self._meta.fields:
                # Get the field name and its value for the current instance
            field_name = field.name
            field_value = getattr(self, field_name)
            # Append field name and value to the email message
            student_message += f"{field_name.capitalize()}: {field_value}\n"
        student_email = self.Current_Enquiry.student_email
        student_email_message = EmailMessage(student_subject, student_message, settings.DEFAULT_FROM_EMAIL, [student_email])
        student_email_message.send()
    
    def save(self, *args, **kwargs):
        # Call the original save method
        super().save(*args, **kwargs)
        
        # Send WhatsApp message
        api_key = "634b7217-d8f7-11ed-a7c7-9606c7e32d76"
        sender_whatsapp_number = "917211117272"
        recipient_whatsapp_number = self.Current_Enquiry.student_phone  # Assuming student_phone contains the WhatsApp number
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
        "placeholders": ["Ramesh", "Hello, your enquiry has been submitted successfully. We will get back to you soon."],
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












