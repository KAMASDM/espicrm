from django.db import models

# Create your models here.
from Master.models import course_levels, intake, Course, university, assessment_status
from DetailEnquiry.models import Detail_Enquiry
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField


class assessment(models.Model):
    assigned_users = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    enquiry = models.ForeignKey(Detail_Enquiry, on_delete=models.CASCADE)
    student_country = CountryField(blank_label="(select country)", blank=True, null=True)
    university = models.ForeignKey(university, on_delete=models.CASCADE, blank=True, null=True)
    level_applying_for = models.ForeignKey(course_levels, on_delete=models.CASCADE, blank=True, null=True)
    course_interested = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    intake_interested = models.ForeignKey(intake, on_delete=models.CASCADE, blank=True, null=True)
    specialisation = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    application_fee = models.CharField(max_length=100, blank=True, null=True)
    tution_fee = models.CharField(max_length=100, blank=True, null=True)
    fee_currency = models.CharField(max_length=100, blank=True, null=True)
    course_link = models.CharField(max_length=200,blank=True, null=True)
    ass_status = models.ForeignKey(assessment_status, blank=True, on_delete=models.CASCADE,null=True)
    notes = models.TextField( blank=True,null=True)

    def __str__(self):
        return self.enquiry

# models.py

from django.db import models
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings



@receiver(models.signals.post_save, sender=assessment)
def send_assessment_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Assessment Submission Confirmation'
        message = f"Dear {instance.student_name},\n\nThank you for submitting your assessment.\n\nSincerely,\nThe Assessment Team"
        from_email = settings.EMAIL_HOST_USER
        to_email = instance.student_email  # Assuming you have a field for student email in your assessment model
        send_mail(subject, message, from_email, [to_email])
