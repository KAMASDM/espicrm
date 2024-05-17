from django.db import models
from Assessment.models import assessment
from Master.models import application_status
from Enquiry.models import enquiry
import requests
# Create your models here.
class Application(models.Model):
    application = models.ForeignKey(assessment, on_delete=models.CASCADE,blank=True)
    sop = models.FileField(upload_to='sop', blank=True)
    cv = models.FileField(upload_to='cv', blank=True)
    passport = models.FileField(upload_to='passport', blank=True)
    ielts = models.FileField(upload_to='ielts', blank=True)
    gre = models.FileField(upload_to='gre', blank=True)
    toefl = models.FileField(upload_to='toefl', blank=True)
    gmat = models.FileField(upload_to='gmat', blank=True)
    pte = models.FileField(upload_to='pte', blank=True)
    work_experience = models.FileField(upload_to='work_experience', blank=True)
    diploma_marksheet = models.FileField(upload_to='diploma_marksheet', blank=True)
    bachelor_marksheet = models.FileField(upload_to='bachelor_marksheet', blank=True)
    master_marksheet = models.FileField(upload_to='master_marksheet', blank=True)
    other_documents = models.FileField(upload_to='other_documents', blank=True)
    # followup = models.ForeignKey(Followup, on_delete=models.SET_NULL, null=True, blank=True)
    application_status = models.ForeignKey(application_status, max_length=100, blank=True, on_delete=models.CASCADE)
    Rejection_reason = models.TextField(blank=True)

    def __str__(self):
        return (f"{self.application}")
    
    # def save(self, *args, **kwargs):
    #     # Call the original save method
    #     super().save(*args, **kwargs)
        
    #     # Send WhatsApp message
    #     api_key = "634b7217-d8f7-11ed-a7c7-9606c7e32d76"
    #     sender_whatsapp_number = "917211117272"
    #     recipient_whatsapp_number =  self.application.enquiry.Current_Enquiry.student_phone  # Assuming student_phone contains the WhatsApp number
    #     student_name = self.application.enquiry.Current_Enquiry.student_First_Name
    #     whatsapp_message = "Hello, your Application has been submitted successfully. We will get back to you soon."
        
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
    #     "placeholders": [student_name,whatsapp_message ],
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














