from django.db import models

# Create your models here.
from Master.models import course_levels, intake, documents_required, course_requirements, current_education, country,enquiry_status, Course, university, intake_Year, assessment_status
from Enquiry.models import enquiry
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField


class assessment(models.Model):
    assigned_users = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    enquiry = models.ForeignKey(enquiry, on_delete=models.CASCADE)

    student_country = CountryField(blank_label="(select country)")
    university = models.ForeignKey(university, on_delete=models.CASCADE)
    level_applying_for = models.ForeignKey(course_levels, on_delete=models.CASCADE)
    course_interested = models.ForeignKey(Course, on_delete=models.CASCADE)
    intake_interested_month = models.ForeignKey(intake, on_delete=models.CASCADE)
    intake_interested_year = models.ForeignKey(intake_Year, on_delete=models.CASCADE)
    specialisation = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    application_fee = models.CharField(max_length=100)
    tution_fee = models.CharField(max_length=100)
    fee_currency = models.CharField(max_length=100)
    course_link = models.CharField(max_length=200)
   # ass_status = models.ForeignKey(assessment_status, blank=True, on_delete=models.CASCADE)
    notes = models.TextField()

    def __str__(self):
        return self.enquiry.student_First_Name

