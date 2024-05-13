from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField
from smart_selects.db_fields import ChainedForeignKey
from django.core.mail import EmailMessage
from django.conf import settings
# Create your models here.
from Master.models import (Available_Services, CountryInterested, Course,
                           Enquiry_Source, course_levels, current_education,
                           enquiry_status, intake, university,EnquiryFollowupStatus)
import requests

# Create your models here.
class enquiry(models.Model):
    # Personal Info
    student_First_Name = models.CharField(max_length=100)
    student_Last_Name = models.CharField(max_length=100)
    student_passport = models.CharField(max_length=100)
    Source_Enquiry = models.ForeignKey(Enquiry_Source, on_delete=models.CASCADE,blank=True,null =True)

    # Contact Info
    student_phone = models.CharField(max_length=100)
    alternate_phone = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_address = models.TextField()
    student_country = CountryField(blank_label="(select country)", default="IN")
    student_state = models.CharField(max_length=100)
    student_city = models.CharField(max_length=100)
    student_zip = models.CharField(max_length=10)

    # Education Info
    current_education = models.ForeignKey(current_education, on_delete=models.CASCADE,null =True,blank=True)

    # Enquiry Info
    country_interested = models.ForeignKey(CountryInterested,on_delete=models.CASCADE,null =True,blank=True)
    university_interested = ChainedForeignKey(
        university,
        chained_field="country_interested",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    course_interested = ChainedForeignKey(
        Course,
        chained_field="university_interested",
        chained_model_field="university",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    level_applying_for = models.ForeignKey(course_levels, on_delete=models.CASCADE,null =True,blank=True)
    intake_interested = models.ForeignKey(intake, on_delete=models.CASCADE,null =True,blank=True)
    Interested_Services = models.ManyToManyField(Available_Services,blank=True, related_name="Interested_Services", default='Counselling')


    # For Counsellor
    assigned_users = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True,blank=True)
    enquiry_status = models.ForeignKey(enquiry_status, on_delete=models.CASCADE,null =True,blank=True)
    EnquiryFollowup = models.ForeignKey(EnquiryFollowupStatus, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField()
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='+',null=True, blank=True)

    def __str__(self):
        return (f"{self.student_First_Name} - {self.country_interested} - {self.level_applying_for} "
                f"- {self.intake_interested}")
        
        
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    
    #     # Send email to admin
    #     admin_subject = "New Detail Enquiry Submitted"
    #     admin_message = (
    #         f"A new Detail enquiry has been submitted with ID: {self.id}."
    #     )
    #     admin_email = settings.ADMIN_EMAIL
    #     admin_email_message = EmailMessage(admin_subject, admin_message, settings.DEFAULT_FROM_EMAIL, [admin_email])
    #     admin_email_message.send()
    
    #     # Send email to student
    #     student_subject = "Thank You for Your Detail Enquiry"
    #     student_message = (
    #         f"Thank you for your  Enquiry. We will get back to you shortly."
    
    
    #     )
    #     for field in self._meta.fields:
    #             # Get the field name and its value for the current instance
    #         field_name = field.name
    #         field_value = getattr(self, field_name)
    #         # Append field name and value to the email message
    #         student_message += f"{field_name.capitalize()}: {field_value}\n"
    #     student_email = self.student_email
    #     student_email_message = EmailMessage(student_subject, student_message, settings.DEFAULT_FROM_EMAIL, [student_email])
    #     student_email_message.send()
        
    # def save(self, *args, **kwargs):
    #     # Call the original save method
    #     super().save(*args, **kwargs)
        
    #     # Send WhatsApp message
    #     api_key = "634b7217-d8f7-11ed-a7c7-9606c7e32d76"
    #     sender_whatsapp_number = "917211117272"
    #     recipient_whatsapp_number = self.student_phone  # Assuming student_phone contains the WhatsApp number
    #     whatsapp_message = "Hello, your enquiry has been submitted successfully. We will get back to you soon."
        
    #     url = "https://wapi.flexiwaba.com/v1/wamessage/sendMessage"
    #     headers = {
    #         "Content-Type": "application/json",
    #         "apiKey": api_key
    #     }
    #     payload = {
    #         "from": sender_whatsapp_number,
    #         "to": recipient_whatsapp_number,
    #         "type": "template",
    #         "message": {
    #     "templateid": "195283",
    #     "url": "https://whatsappdata.s3.ap-south-1.amazonaws.com/userMedia/831c2f88a604a07ca94314b56a4921b8/testing_image.jpeg",
    #     "placeholders": [self.student_First_Name,whatsapp_message],
    #     "buttons": [{
    #         "index": 0,
    #         "type": "visit_website",
    #         "placeholder": "visitors-visa"
    #     }]
    # }
    #     }

    #     response = requests.post(url, json=payload, headers=headers)
    #     if response.status_code == 200:
    #         print("WhatsApp message sent successfully")
    #     else:
    #         print("Failed to send WhatsApp message")
        
    
        


