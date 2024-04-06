from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
from Master.models import (Available_Services, CountryInterested, Course,
                           Enquiry_Source, course_levels, current_education,
                           enquiry_status, intake, university)


# Create your models here.
class enquiry(models.Model):
    # Personal Info
    student_First_Name = models.CharField(max_length=100)
    student_Last_Name = models.CharField(max_length=100)
    student_passport = models.CharField(max_length=100)
    Source_Enquiry = models.ForeignKey(Enquiry_Source, on_delete=models.CASCADE,blank=True, default='Website')

    # Contact Info
    student_phone = models.CharField(max_length=10)
    alternate_phone = models.CharField(max_length=10)
    student_email = models.EmailField()
    student_address = models.TextField()
    student_country = CountryField(blank_label="(select country)", default="IN")
    student_state = models.CharField(max_length=100)
    student_city = models.CharField(max_length=100)
    student_zip = models.CharField(max_length=10)

    # Education Info
    current_education = models.ForeignKey(current_education, on_delete=models.CASCADE)

    # Enquiry Info
    country_interested = models.ForeignKey(CountryInterested,on_delete=models.CASCADE)
    university_interested = ChainedForeignKey(
        university,
        chained_field="country_interested",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
    )
    course_interested = ChainedForeignKey(
        Course,
        chained_field="university_interested",
        chained_model_field="university",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
    )
    level_applying_for = models.ForeignKey(course_levels, on_delete=models.CASCADE)
    intake_interested = models.ForeignKey(intake, on_delete=models.CASCADE)
    Interested_Services = models.ManyToManyField(Available_Services,blank=True, related_name="Interested_Services", default='Counselling')


    # For Counsellor
    assigned_users = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    enquiry_status = models.ForeignKey(enquiry_status, on_delete=models.CASCADE)
    notes = models.TextField()

    def __str__(self):
        return (f"{self.student_First_Name} - {self.country_interested} - {self.level_applying_for} "
                f"- {self.intake_interested}")


