from django.db import models

# Create your models here.
from Master.models import course_levels, intake, documents_required, course_requirements, current_education, country, enquiry_status, Course, university, intake_Year
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
    intake_interested_month = models.ForeignKey(intake, on_delete=models.CASCADE)
    intake_interested_year = models.ForeignKey(intake_Year, on_delete=models.CASCADE)

    # For Counsellor
    assigned_users = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default="")
    enquiry_status = models.ForeignKey(enquiry_status, on_delete=models.CASCADE)
    notes = models.TextField()
    report = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.student_First_Name
    
# @receiver(post_save, sender=Enquiry)
# def generate_enquiry_report(sender, instance, created, **kwargs):
#     if created:
#         instance.report = f"Enquiry Report\n\n"
#         instance.report += f"Student Name: {instance.student_First_Name} {instance.student_Last_Name}\n"
#         instance.report += f"Student Email: {instance.student_email}\n"
#         instance.report += f"Country Interested: {instance.country_interested}\n"
#         instance.report += f"University Interested: {instance.university_interested}\n"
#         instance.report += f"Course Interested: {instance.course_interested}\n"
#         instance.report += f"Level Applying For: {instance.level_applying_for}\n"
#         instance.report += f"Intake Interested: {instance.intake_interested_month} {instance.intake_interested_year}\n"
#         # Add more fields as needed
#         instance.save()

