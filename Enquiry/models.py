from django.db import models

# Create your models here.
from Master.models import course_levels, intake, current_education, enquiry_status, Course, university
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField


# Create your models here.
class enquiry(models.Model):
    # Personal Info
    student_First_Name = models.CharField(max_length=100,null=False, blank=False,)
    student_Last_Name = models.CharField(max_length=100,null=False, blank=False)
    student_passport = models.CharField(max_length=100,null=False, blank=False)

    # Contact Info
    student_phone = models.CharField(max_length=10,null=False, blank=False)
    alternate_phone = models.CharField(max_length=10,null=True, blank=True)
    student_email = models.EmailField(max_length=100,null=False, blank=False)
    student_address = models.TextField(max_length=200,null=False, blank=False)
    student_country = CountryField(blank_label="(select country)",null=False, blank=False)
    student_state = models.CharField(max_length=100,null=False, blank=False)
    student_city = models.CharField(max_length=100,null=False, blank=False)
    student_zip = models.CharField(max_length=10,null=False, blank=False)

    # Education Info
    current_education = models.ForeignKey(current_education, on_delete=models.CASCADE)

    # Enquiry Info
    country_interested = CountryField()
    university_interested = models.ForeignKey(university, on_delete=models.CASCADE)
    course_interested = models.ForeignKey(Course, on_delete=models.CASCADE)
    level_applying_for = models.ForeignKey(course_levels, on_delete=models.CASCADE)
    intake_interested = models.ForeignKey(intake, on_delete=models.CASCADE)


    # For Counsellor
    assigned_users = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default="")
    enquiry_status = models.ForeignKey(enquiry_status, on_delete=models.CASCADE)
    notes = models.TextField()
    report = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.student_First_Name

