from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
from Master.models import course_levels, intake, Course, university, assessment_status, CountryInterested
from DetailEnquiry.models import Detail_Enquiry
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField

from django.core.mail import EmailMessage
from django.conf import settings
class assessment(models.Model):
    assigned_users = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    enquiry = models.ForeignKey(Detail_Enquiry, on_delete=models.CASCADE)
    student_country = models.ForeignKey(CountryInterested, on_delete=models.CASCADE, blank=True,)
    university = ChainedForeignKey(
        university,
        chained_field="student_country",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
        sort=True,)
    level_applying_for = models.ForeignKey(course_levels, on_delete=models.CASCADE, blank=True, null=True)
    course_interested = ChainedForeignKey(
        Course,
        chained_field="university",
        chained_model_field="university",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
    )
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
        return (f"{self.enquiry}")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Send email to admin
        admin_subject = "New Assessment Created"
        admin_message = (
            f"A new assessment has been created with ID: {self.id}.\n"
            f"Enquiry ID: {self.enquiry.id}\n"
            f"Assigned User: {self.assigned_users}\n"
            f"Student Country: {self.student_country}\n"
            f"University: {self.university}\n"
            f"Level Applying For: {self.level_applying_for}\n"
            f"Course Interested: {self.course_interested}\n"
            f"Intake Interested: {self.intake_interested}\n"
            f"Specialisation: {self.specialisation}\n"
            f"Duration: {self.duration}\n"
            f"Application Fee: {self.application_fee}\n"
            f"Tution Fee: {self.tution_fee}\n"
            f"Fee Currency: {self.fee_currency}\n"
            f"Course Link: {self.course_link}\n"
            f"Assessment Status: {self.ass_status}\n"
            f"Notes: {self.notes}"
        )
        admin_email = settings.ADMIN_EMAIL
        admin_email_message = EmailMessage(admin_subject, admin_message, settings.DEFAULT_FROM_EMAIL, [admin_email])
        admin_email_message.send()

        # Send email to assigned user
        assigned_user_email = self.assigned_users.email
        user_subject = "New Assessment Assigned"
        user_message = (
            f"A new assessment has been assigned to you. Details:\n"
            f"Enquiry ID: {self.enquiry.id}\n"
            f"Student Country: {self.student_country}\n"
            f"University: {self.university}\n"
            f"Level Applying For: {self.level_applying_for}\n"
            f"Course Interested: {self.course_interested}\n"
            f"Intake Interested: {self.intake_interested}\n"
            f"Specialisation: {self.specialisation}\n"
            f"Duration: {self.duration}\n"
            f"Application Fee: {self.application_fee}\n"
            f"Tution Fee: {self.tution_fee}\n"
            f"Fee Currency: {self.fee_currency}\n"
            f"Course Link: {self.course_link}\n"
            f"Assessment Status: {self.ass_status}\n"
            f"Notes: {self.notes}"
        )
        user_email_message = EmailMessage(user_subject, user_message, settings.DEFAULT_FROM_EMAIL, [assigned_user_email])
        user_email_message.send()
    
    

