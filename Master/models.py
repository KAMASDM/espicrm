from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField

#from Master.models import Toefl_Exam, ielts_Exam, PTE_Exam, Duolingo_Exam, Gre_Exam, Gmat_Exam, bachelor_requirement


from django.core.validators import MinValueValidator, MaxValueValidator




class CountryInterested(models.Model):
    country = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.country

# Create your models here.
class country(models.Model):
    country = CountryField(blank_label="(select country)")
    def __str__(self):
        return self.country

class course_levels(models.Model):

    levels = models.CharField(max_length=100)
    def __str__(self):
        return self.levels

class Available_Services(models.Model):
        Services = models.CharField(max_length=100)
        Price = models.FloatField(blank=True, null=True, help_text="Price in INR")

        def __str__(self):
            return (f"{self.Services}")


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
    country = models.ForeignKey(CountryInterested,on_delete=models.CASCADE)
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
    intake = models.ManyToManyField(intake)
    documents_required = models.ManyToManyField(documents_required)
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
    level = models.CharField(max_length=100,blank=True, null=True)
    Stream = models.CharField(max_length=100,blank=True, null=True)
    Percentage = models.FloatField(blank=True)
    Year_of_Passing = models.IntegerField(blank=True)
    Name_of_Institute = models.CharField(max_length=100,blank=True)
    Medium_of_Education = models.CharField(max_length=100,blank=True)
    Board = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.level

class Work_Experience(models.Model):
    Company_Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    def __str__(self):
        return self.Company_Name

class Ielts_Exam(models.Model):
    Listening = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)], null=True)
    Reading = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)], null=True)
    Writing = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)], null=True)
    Speaking = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)], null=True)
    Overall = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)], null=True)

    def __str__(self):
        return f"IELTS Overall: {self.Overall}"

class Toefl_Exam(models.Model):
    Listening = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    Reading = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    Writing = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    Speaking = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    Overall = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(120)])

    def __str__(self):
        return f"Toefl Overall: {self.Overall}"

class PTE_Exam(models.Model):
    Listening = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(90)])
    Reading = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(90)])
    Writing = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(90)])
    Speaking = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(90)])
    Overall = models.FloatField(validators=[MinValueValidator(10), MaxValueValidator(90)])

    def __str__(self):
        return f"PTE Overall: {self.Overall}"

class Duolingo_Exam(models.Model):
    Overall = models.FloatField(validators=[MinValueValidator(10), MaxValueValidator(160)])

    def __str__(self):
        return f"Duolingo Overall: {self.Overall}"

class Gre_Exam(models.Model):
    Verbal = models.FloatField(validators=[MinValueValidator(130), MaxValueValidator(170)])
    Quantitative = models.FloatField(validators=[MinValueValidator(130), MaxValueValidator(170)])
    Analytical = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    Overall = models.FloatField(validators=[MinValueValidator(260), MaxValueValidator(340)])

    def __str__(self):
        return f"GRE Overall: {self.Overall}"

class Gmat_Exam(models.Model):
    Verbal = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    Quantitative = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    Analytical = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    Overall = models.FloatField(validators=[MinValueValidator(200), MaxValueValidator(800)])

    def __str__(self):
        return f"GMAT Overall: {self.Overall}"

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
    Refusal_Reason = models.TextField()
    Refusal_Country = CountryField()
    Refusal_Visa_Category = models.CharField(max_length=100)
    Refusal_Date = models.DateField()
    Refusal_Letter = models.FileField(upload_to='refusal_letter/', blank=True)


    def __str__(self):
        return f"{self.Refusal_Reason}"

class Detail_Enquiry_Status(models.Model):
    Status = models.CharField(max_length=100)
    def __str__(self):
        return self.Status


class Enquiry_Source(models.Model):
    Source = models.CharField(max_length=100)
    Reference_Number = models.CharField(max_length=100)
    def __str__(self):
        return self.Source

class Payment_Type(models.Model):
    Type = models.CharField(max_length=100)
    def __str__(self):
        return self.Type

class Payment_Status(models.Model):
    Status = models.CharField(max_length=100)
    def __str__(self):
        return self.Status

class Payment_Mode(models.Model):
    Mode = models.CharField(max_length=100)
    def __str__(self):
        return self.Mode
    


# class Followup_status(models.Model):
#     FREQUENCY_CHOICES = [
#         (1, '1 day'),
#         (2, '2 days'),
#         (3, '3 days'),
#     ]

#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('Completed', 'Completed'),
#         ('Cancelled', 'Cancelled'),
#     ]

#     model_choices = [
#         ('Enquiry', 'Enquiry'),
#         ('Application', 'Application'),
#         ('Assessment', 'Assessment'),
#         ('Payment', 'Payment'),
#     ]

#     model = models.CharField(max_length=100, choices=model_choices)
#     frequency = models.IntegerField(choices=FREQUENCY_CHOICES)
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     reminder = models.BooleanField(default=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

#     def __str__(self):
#         return f"{self.get_model_display()} Followup for {self.user.username}"


from django.db import models
from django.contrib.auth import get_user_model

INTERACTION_CHOICES = [
        ('call', 'Call'),
        ('meeting', 'Meeting'),
        ('email', 'Email'),
        ('other', 'Other'),
    ]

FOLLOWUP_METHOD_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('sms', 'SMS'),
        ('other', 'Other'),
    ]

PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
]

STATUS_CHOICES = [
        ('open', 'Open'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
]

REMINDER_FREQUENCY_CHOICES = [
        ('one-time', 'One-time'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        # Add more choices as needed
    ]

    

class EnquiryFollowupStatus(models.Model):
    last_contact_date = models.DateField(null=True, blank=True)
    last_interaction_summary = models.TextField(blank=True)
    last_interaction_type = models.CharField(max_length=20, choices=INTERACTION_CHOICES, blank=True)

    next_followup_date = models.DateField(null=True, blank=True)
    next_followup_purpose = models.TextField(blank=True)
    next_followup_method = models.CharField(max_length=20, choices=FOLLOWUP_METHOD_CHOICES, blank=True)

    reminder_date_time = models.DateTimeField(null=True, blank=True)
    reminder_frequency = models.CharField(max_length=20, choices=REMINDER_FREQUENCY_CHOICES, blank=True)
    reminder_notification_method = models.CharField(max_length=20, choices=FOLLOWUP_METHOD_CHOICES, blank=True)

    priority_level = models.CharField(max_length=20, choices=PRIORITY_CHOICES, blank=True)
    urgency = models.CharField(max_length=20, blank=True)

    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    outcome = models.TextField(blank=True)

    attachment_enquiryFollowup = models.FileField(upload_to='attachmentsForEnquiryFollowup/', blank=True)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_contact_date} Followup Status"



class DetailEnquiryFollowupStatus(models.Model):
    last_contact_date = models.DateField(null=True, blank=True)
    last_interaction_summary = models.TextField(blank=True)
    last_interaction_type = models.CharField(max_length=20, choices=INTERACTION_CHOICES, blank=True)

    next_followup_date = models.DateField(null=True, blank=True)
    next_followup_purpose = models.TextField(blank=True)
    next_followup_method = models.CharField(max_length=20, choices=FOLLOWUP_METHOD_CHOICES, blank=True)

    reminder_date_time = models.DateTimeField(null=True, blank=True)
    reminder_frequency = models.CharField(max_length=20, choices=REMINDER_FREQUENCY_CHOICES, blank=True)
    reminder_notification_method = models.CharField(max_length=20, choices=FOLLOWUP_METHOD_CHOICES, blank=True)

    priority_level = models.CharField(max_length=20, choices=PRIORITY_CHOICES, blank=True)
    urgency = models.CharField(max_length=20, blank=True)

    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    outcome = models.TextField(blank=True)

    attachment_DetailEnquiryFollowup = models.FileField(upload_to='attachmentsForDetailEnquiryFollowup/', blank=True)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"{self.last_contact_date} Followup Status"


class AssesmentFollowupStatus(models.Model):
    last_contact_date = models.DateField(null=True, blank=True)
    last_interaction_summary = models.TextField(blank=True)
    last_interaction_type = models.CharField(max_length=20, choices=INTERACTION_CHOICES, blank=True)

    next_followup_date = models.DateField(null=True, blank=True)
    next_followup_purpose = models.TextField(blank=True)
    next_followup_method = models.CharField(max_length=20, choices=FOLLOWUP_METHOD_CHOICES, blank=True)

    reminder_date_time = models.DateTimeField(null=True, blank=True)
    reminder_frequency = models.CharField(max_length=20, choices=REMINDER_FREQUENCY_CHOICES, blank=True)
    reminder_notification_method = models.CharField(max_length=20, choices=FOLLOWUP_METHOD_CHOICES, blank=True)

    priority_level = models.CharField(max_length=20, choices=PRIORITY_CHOICES, blank=True)
    urgency = models.CharField(max_length=20, blank=True)

    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    outcome = models.TextField(blank=True)

    attachment_AssesmentFollowup = models.FileField(upload_to='attachmentsForAssesmentFollowup/', blank=True)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"{self.last_contact_date} Followup Status"

class PaymentFollowupStatus(models.Model):
    last_contact_date = models.DateField(null=True, blank=True)
    last_interaction_summary = models.TextField(blank=True)
    last_interaction_type = models.CharField(max_length=20, choices=INTERACTION_CHOICES, blank=True)

    next_followup_date = models.DateField(null=True, blank=True)
    next_followup_purpose = models.TextField(blank=True)
    next_followup_method = models.CharField(max_length=20, choices=FOLLOWUP_METHOD_CHOICES, blank=True)

    reminder_date_time = models.DateTimeField(null=True, blank=True)
    reminder_frequency = models.CharField(max_length=20, choices=REMINDER_FREQUENCY_CHOICES, blank=True)
    reminder_notification_method = models.CharField(max_length=20, choices=FOLLOWUP_METHOD_CHOICES, blank=True)

    priority_level = models.CharField(max_length=20, choices=PRIORITY_CHOICES, blank=True)
    urgency = models.CharField(max_length=20, blank=True)

    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    outcome = models.TextField(blank=True)

    attachment_PaymentFollowup = models.FileField(upload_to='attachmentsForPaymentFollowup/', blank=True)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"{self.last_contact_date} Followup Status"