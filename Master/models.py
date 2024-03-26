from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
#from Master.models import Toefl_Exam, ielts_Exam, PTE_Exam, Duolingo_Exam, Gre_Exam, Gmat_Exam, bachelor_requirement


# Create your models here.
class country(models.Model):
    country = CountryField(blank_label="(select country)")
    def __str__(self):
        return self.country

class course_levels(models.Model):

    levels = models.CharField(max_length=100)
    def __str__(self):
        return self.levels


class current_education(models.Model):

    current_education = models.CharField(max_length=100)
    def __str__(self):
        return self.current_education

class intake(models.Model):
    intake_Name = models.CharField(max_length=100)
    intake_month = models.CharField(max_length=10)
    intake_year = models.CharField(max_length=10)

    def __str__(self):
        return self.intake_Name




class documents_required(models.Model):

    docu_name = models.CharField(max_length=100)
    def __str__(self):
        return self.docu_name

class course_requirements(models.Model):

    requirement = models.CharField(max_length=100)
    def __str__(self):
        return self.requirement

class enquiry_status(models.Model):
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.status


class assessment_status(models.Model):
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.status
class application_status(models.Model):
    App_status = models.CharField(max_length=20)
    def __str__(self):
        return self.App_status

class university(models.Model):

    univ_name = models.CharField(max_length=100)
    country = CountryField(blank_label="(select country)", blank=True, null=True)
    univ_desc = models.CharField(max_length=1000, blank=True, null=True)
    univ_logo = models.ImageField(upload_to="media", blank=True, null=True)
    univ_phone = models.CharField(max_length=10, blank=True, null=True)
    univ_email = models.EmailField(max_length=254, blank=True, null=True)
    univ_website = models.URLField(blank=True, null=True)
    tenth_std_percentage_requirement = models.ForeignKey("Master.tenth_std_percentage_requirement",
                                                         on_delete=models.CASCADE, blank=True, null=True)
    twelfth_std_percentage_requirement = models.ForeignKey("Master.twelfth_std_percentage_requirement",
                                                           on_delete=models.CASCADE, blank=True, null=True)
    bachelor_requirement = models.ForeignKey("Master.bachelor_requirement", on_delete=models.CASCADE, blank=True, null=True)
    masters_requirement = models.ForeignKey("Master.masters_requirement", on_delete=models.CASCADE, blank=True, null=True)
    Toefl_Exam = models.ForeignKey("Master.Toefl_Exam", on_delete=models.CASCADE, blank=True, null=True)
    ielts_Exam = models.ForeignKey("Master.ielts_Exam", on_delete=models.CASCADE, blank=True, null=True)
    PTE_Exam = models.ForeignKey("Master.PTE_Exam", on_delete=models.CASCADE, blank=True, null=True)
    Duolingo_Exam = models.ForeignKey("Master.Duolingo_Exam", on_delete=models.CASCADE, blank=True, null=True)
    Gre_Exam = models.ForeignKey("Master.Gre_Exam", on_delete=models.CASCADE, blank=True, null=True)
    Gmat_Exam = models.ForeignKey("Master.Gmat_Exam", on_delete=models.CASCADE, blank=True, null=True)
    Remark = models.TextField(blank=True, verbose_name="Notes", null=True)
    Active = models.BooleanField()
    newsletter = models.FileField(upload_to='newsletter/',blank=True, verbose_name="Newsletters", null=True)
    application_form = models.FileField(upload_to='application_forms/', blank=True, verbose_name="Application Form", null=True)
    assigned_users = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default="", blank=True, null=True)

    def __str__(self):
        return self.univ_name



class Course(models.Model):

    university = models.ForeignKey(university, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    course_levels = models.ForeignKey(course_levels, on_delete=models.CASCADE, blank=True, null=True)
    intake = models.ManyToManyField(intake,blank=True, null=True)
    documents_required = models.ManyToManyField(documents_required,blank=True, null=True)
    tenth_std_percentage_requirement = models.ForeignKey("Master.tenth_std_percentage_requirement", on_delete=models.CASCADE, blank=True, null=True)
    twelfth_std_percentage_requirement = models.ForeignKey("Master.twelfth_std_percentage_requirement", on_delete=models.CASCADE,blank=True, null=True)
    bachelor_requirement = models.ForeignKey("Master.bachelor_requirement", on_delete=models.CASCADE,blank=True, null=True)
    masters_requirement = models.ForeignKey("Master.masters_requirement", on_delete=models.CASCADE,blank=True, null=True)
    Toefl_Exam = models.ForeignKey("Master.Toefl_Exam", on_delete=models.CASCADE,blank=True, null=True)
    ielts_Exam = models.ForeignKey("Master.ielts_Exam", on_delete=models.CASCADE,blank=True, null=True)
    PTE_Exam = models.ForeignKey("Master.PTE_Exam", on_delete=models.CASCADE,blank=True,null=True)
    Duolingo_Exam = models.ForeignKey("Master.Duolingo_Exam", on_delete=models.CASCADE,blank=True,null=True)
    Gre_Exam = models.ForeignKey("Master.Gre_Exam", on_delete=models.CASCADE,blank=True,null=True)
    Gmat_Exam = models.ForeignKey("Master.Gmat_Exam", on_delete=models.CASCADE,blank=True,null=True)
    Remark = models.TextField(blank=True, verbose_name="Notes", null=True)

    Active = models.BooleanField()

    def __str__(self):
        return (f"{self.course_name} - {self.university}")

class Edu_Level(models.Model):
    level = models.CharField(max_length=100)
    Stream = models.CharField(max_length=100)
    Percentage = models.FloatField()
    Year_of_Passing = models.IntegerField()
    Name_of_Institute = models.CharField(max_length=100)
    Medium_of_Education = models.CharField(max_length=100)
    Board = models.CharField(max_length=100)
    def __str__(self):
        return self.level

class Work_Experience(models.Model):
    Company_Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    def __str__(self):
        return self.Company_Name
# class ielts_Exam(models.Model):
#     Listening = models.FloatField()
#     Reading = models.FloatField()
#     Writing = models.FloatField()
#     Speaking = models.FloatField()
#     Overall = models.FloatField()
#     def __str__(self):
#         return self.Overall

# class Toefl_Exam(models.Model):
#     Listening = models.FloatField()
#     Reading = models.FloatField()
#     Writing = models.FloatField()
#     Speaking = models.FloatField()
#     Overall = models.FloatField()
#     def __str__(self):
#         return (self.Overall)


class ielts_Exam(models.Model):
    Listening = models.FloatField(null=True)
    Reading = models.FloatField(null=True)
    Writing = models.FloatField(null=True)
    Speaking = models.FloatField(null=True)
    Overall = models.FloatField(null=True)
    def __str__(self):
        return f"ielts Exam: Overall - {self.Overall}"

class Toefl_Exam(models.Model):
    Listening = models.FloatField()
    Reading = models.FloatField()
    Writing = models.FloatField()
    Speaking = models.FloatField()
    Overall = models.FloatField()

    def __str__(self):
        return f"Toefl Exam: Overall - {self.Overall}"

class PTE_Exam(models.Model):
    Listening = models.FloatField()
    Reading = models.FloatField()
    Writing = models.FloatField()
    Speaking = models.FloatField()
    Overall = models.FloatField()

    def __str__(self):
        return f"PTE Exam: Overall - {self.Overall}"



class Duolingo_Exam(models.Model):
    Overall = models.FloatField()

    def __str__(self):
        return f"Duolingo Exam: Overall - {self.Overall}"


class Gre_Exam(models.Model):
    Verbal = models.FloatField()
    Quantitative = models.FloatField()
    Analytical = models.FloatField()
    Overall = models.FloatField()
    def __str__(self):
        return f"Gre Exam: Overall - {self.Overall}"


class Gmat_Exam(models.Model):
    Verbal = models.FloatField()
    Quantitative = models.FloatField()
    Analytical = models.FloatField()
    Overall = models.FloatField()
    def __str__(self):
        return f"Gmat Exam: Overall - {self.Overall}"

class tenth_std_percentage_requirement(models.Model):
    percentage = models.FloatField()
    def __str__(self):
        return f"Required: {self.percentage}"

class twelfth_std_percentage_requirement(models.Model):
    percentage = models.FloatField()

    def __str__(self):
        return f"Required: {self.percentage}"

class bachelor_requirement(models.Model):
    requirement = models.CharField(max_length=100)

    def __str__(self):
        return f"Required: {self.requirement}"


class masters_requirement(models.Model):
    requirement = models.CharField(max_length=100)

    def __str__(self):
        return f"Required: {self.requirement}"

class Rejection_Reason(models.Model):
    Refusal_Reason = models.TextField(null=True, blank=True)
    Refusal_Country = CountryField()
    Refusal_Visa_Category = models.CharField(max_length=100)
    Refusal_Date = models.DateField()
    Refusal_Letter = models.FileField(upload_to='refusal_letter/', blank=True)



    def __str__(self):
        return self.Refusal_Reason


#add a field to class Rejection_Reason which is a file field to upload the refusal letter

from Enquiry.models import enquiry
from DetailEnquiry.models import Detail_Enquiry
from Assessment.models import assessment

class Report(models.Model):
    ENQUIRY = 'Enquiry'
    DETAIL_ENQUIRY = 'Detail_enquiry'
    ASSESSMENT = 'assessment'

    REPORT_TYPE_CHOICES = [
        (ENQUIRY, 'Enquiry'),
        (DETAIL_ENQUIRY, 'Detail Enquiry'),
        (ASSESSMENT, 'assessment'),
    ]

    enquiry = models.ForeignKey(enquiry, related_name='reports', on_delete=models.CASCADE, null=True, blank=True)
    detail_enquiry = models.ForeignKey(Detail_Enquiry, related_name='reports', on_delete=models.CASCADE, null=True, blank=True)
    assessment = models.ForeignKey(assessment, related_name='reports', on_delete=models.CASCADE, null=True, blank=True)
    report_file = models.FileField(upload_to='reports/')
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.enquiry:
            return f"Report for Enquiry: {self.enquiry.student_First_Name} - {self.created_at}"
        elif self.detail_enquiry:
            return f"Report for Detail Enquiry: {self.detail_enquiry.name} - {self.created_at}"
        elif self.assessment:
            return f"Report for Assessment: {self.assessment.name} - {self.created_at}"
        else:
            return "Unknown Report"

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.enquiry:
                self.report_type = self.ENQUIRY
            elif self.detail_enquiry:
                self.report_type = self.DETAIL_ENQUIRY
            elif self.assessment:
                self.report_type = self.ASSESSMENT
        super().save(*args, **kwargs)



