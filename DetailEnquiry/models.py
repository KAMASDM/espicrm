from django.db import models

# Create your models here.
from Enquiry.models import enquiry
from Master.models import (Edu_Level, Work_Experience, Toefl_Exam, ielts_Exam, PTE_Exam,
                           Duolingo_Exam, Gre_Exam, Gmat_Exam, Rejection_Reason, Available_Services,Detail_Enquiry_Status)
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
class Detail_Enquiry(models.Model):

    Current_Enquiry = models.ForeignKey(enquiry, on_delete=models.CASCADE)
    Current_Education_Details = models.ForeignKey(Edu_Level, on_delete=models.CASCADE, blank=True, null=True)
    Tenth_Education_Details = models.ForeignKey(Edu_Level, on_delete=models.CASCADE, blank=True, null=True, related_name='Tenth_Education_Details')
    Twelveth_Education_Details = models.ForeignKey(Edu_Level, on_delete=models.CASCADE, blank=True, null=True, related_name='Twelveth_Education_Details')
    Graduation_Education_Details = models.ForeignKey(Edu_Level, on_delete=models.CASCADE, blank=True, null=True, related_name='Graduation_Education_Details')
    Work_Experience = models.ForeignKey(Work_Experience,max_length=100, on_delete=models.CASCADE, blank=True, null=True)
    Toefl_Exam = models.ForeignKey(Toefl_Exam, on_delete=models.CASCADE, blank=True, null=True)
    ielts_Exam = models.ForeignKey(ielts_Exam, on_delete=models.CASCADE, blank=True, null=True)
    PTE_Exam = models.ForeignKey(PTE_Exam, on_delete=models.CASCADE, blank=True, null=True)
    Duolingo_Exam = models.ForeignKey(Duolingo_Exam, on_delete=models.CASCADE, blank=True, null=True)
    Gre_Exam = models.ForeignKey(Gre_Exam, on_delete=models.CASCADE, blank=True, null=True)
    Gmat_Exam = models.ForeignKey(Gmat_Exam, on_delete=models.CASCADE, blank=True, null=True)
    Father_Occupation = models.CharField(max_length=100, blank=True, null=True)
    Father_Annual_Income = models.FloatField(blank=True, null=True)
    Refusal = models.ForeignKey(Rejection_Reason, on_delete=models.CASCADE, blank=True, null=True)
    Twelveth_Document = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])] ,blank=True)
    Tenth_Document = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], blank=True)
    Graduation_Marksheet = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], blank=True)
    Graduation_Certificate = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], blank=True)
    UG_Marksheet = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], blank=True)
    UG_Certificate = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])] ,blank=True)
    Work_Experience_Document = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], blank=True)
    Passport_Document = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])] ,blank=True)
    Offer_Letter = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])] ,blank=True)
    Ielts_Result = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], blank=True)
    Toefl_Result = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], blank=True)
    PTE_Result = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], blank=True)
    Duolingo_Result = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], blank=True)
    Gre_Result = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], blank=True)
    Gmat_Result = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], blank=True)
    Confirmed_Services = models.ManyToManyField(Available_Services, blank=True)
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
        
    












