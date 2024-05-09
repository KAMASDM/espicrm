from django.db import models
from Master.models import Payment_Type, Payment_Status, Payment_Mode,Available_Services,PaymentFollowupStatus
from DetailEnquiry.models import Detail_Enquiry
from django.contrib.auth import get_user_model
import requests
# Create your models here.
class Payment(models.Model):
    Memo_For = models.ForeignKey(Detail_Enquiry, on_delete=models.CASCADE,null=True,blank=True,)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    Payment_Type = models.ForeignKey(Payment_Type,on_delete=models.CASCADE, blank=True,null=True,)
    Payment_For = models.ManyToManyField(Available_Services, blank=True,null=True,)
    payment_date = models.DateField(blank=True, null=True, editable=True)
    payment_amount = models.FloatField(blank=True, null=True)
    payment_mode = models.ForeignKey(Payment_Mode,on_delete=models.CASCADE, blank=True)
    payment_status = models.ForeignKey(Payment_Status, on_delete=models.CASCADE,blank=True)
    payment_reference = models.CharField(max_length=100, blank=True, null=True)
    payment_remarks = models.TextField(blank=True, null=True)
    payment_received_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default="",blank=True, null=True)
    payment_document = models.FileField(upload_to='documents/', blank=True)
    PaymentFollowup = models.ForeignKey(PaymentFollowupStatus, on_delete=models.SET_NULL, null=True, blank=True)
    

   # payment_user = models.ForeignKey('Accounts.CustomUser', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return (f"{self.payment_id}")
    
    
    # def save(self, *args, **kwargs):
    #         # Call the original save method
    #     super().save(*args, **kwargs)
        
    #     # Send WhatsApp message
    #     api_key = "634b7217-d8f7-11ed-a7c7-9606c7e32d76"
    #     sender_whatsapp_number = "917211117272"
    #     recipient_whatsapp_number = self.Memo_For.Current_Enquiry.student_phone
    #     student_name=self.Memo_For.Current_Enquiry.student_First_Name 
    #     whatsapp_message = "Hello, your Payment has been submitted successfully. We will get back to you soon."
        
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
    #     "placeholders": [student_name, whatsapp_message],
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
    
    
    
