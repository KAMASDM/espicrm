from django.db import models

# Create your models here.
from Master.models import course_levels, intake, documents_required, course_requirements, current_education, country, enquiry_status, Course, university, intake_Year
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField


# Create your models here.
class enquiry(models.Model):
    # Personal Info
    student_First_Name = models.CharField(max_length=100)
    student_Last_Name = models.CharField(max_length=100)
    student_passport = models.CharField(max_length=100)

    # Contact Info
    student_phone = models.CharField(max_length=10)
    alternate_phone = models.CharField(max_length=10)
    student_email = models.EmailField()
    student_address = models.TextField()
    student_country = CountryField(blank_label="(select country)")
    student_state = models.CharField(max_length=100)
    student_city = models.CharField(max_length=100)
    student_zip = models.CharField(max_length=10)

    # Education Info
    current_education = models.ForeignKey(current_education, on_delete=models.CASCADE)

    # Enquiry Info
    country_interested = CountryField()
    university_interested = models.ForeignKey(university, on_delete=models.CASCADE)
    course_interested = models.ForeignKey(Course, on_delete=models.CASCADE)
    level_applying_for = models.ForeignKey(course_levels, on_delete=models.CASCADE)
    intake_interested_month = models.ForeignKey(intake, on_delete=models.CASCADE)
    intake_interested_year = models.ForeignKey(intake_Year, on_delete=models.CASCADE)

    # For Counsellor
    assigned_users = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default="")
    enquiry_status = models.ForeignKey(enquiry_status, on_delete=models.CASCADE)
    notes = models.TextField()

    def __str__(self):
        return self.student_First_Name
