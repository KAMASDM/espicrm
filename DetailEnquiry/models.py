from django.db import models

# Create your models here.
from Enquiry.models import enquiry
from Master.models import Edu_Level, Work_Experience, Toefl_Exam, ielts_Exam, PTE_Exam, Duolingo_Exam, Gre_Exam, Gmat_Exam, Rejection_Reason

class Detail_Enquiry(models.Model):

    Current_Enquiry = models.ForeignKey(enquiry, on_delete=models.CASCADE)
    level = models.ForeignKey(Edu_Level, on_delete=models.CASCADE)
    Work_Experience = models.ForeignKey(Work_Experience,max_length=100, on_delete=models.CASCADE)
    Toefl_Exam = models.ForeignKey(Toefl_Exam, on_delete=models.CASCADE)
    ielts_Exam = models.ForeignKey(ielts_Exam, on_delete=models.CASCADE)
    PTE_Exam = models.ForeignKey(PTE_Exam, on_delete=models.CASCADE)
    Duolingo_Exam = models.ForeignKey(Duolingo_Exam, on_delete=models.CASCADE)
    Gre_Exam = models.ForeignKey(Gre_Exam, on_delete=models.CASCADE)
    Gmat_Exam = models.ForeignKey(Gmat_Exam, on_delete=models.CASCADE)
    Father_Occupation = models.CharField(max_length=100)
    Father_Annual_Income = models.FloatField()
    Refusal = models.ForeignKey(Rejection_Reason, on_delete=models.CASCADE,null=True)
    Twelveth_Document = models.FileField(upload_to='documents/')
    Tenth_Document = models.FileField(upload_to='documents/')
    Graduation_Marksheet = models.FileField(upload_to='documents/')
    Graduation_Certificate = models.FileField(upload_to='documents/')

    UG_Marksheet = models.FileField(upload_to='documents/')
    UG_Certificate = models.FileField(upload_to='documents/')

    Work_Experience_Document = models.FileField(upload_to='documents/')
    Passport_Document = models.FileField(upload_to='documents/')
    Offer_Letter = models.FileField(upload_to='documents/')
    Ielts_Result = models.FileField(upload_to='documents/')
    Toefl_Result = models.FileField(upload_to='documents/')
    PTE_Result = models.FileField(upload_to='documents/')
    Duolingo_Result = models.FileField(upload_to='documents/')
    Gre_Result = models.FileField(upload_to='documents/')
    Gmat_Result = models.FileField(upload_to='documents/')


    def __str__(self):
        return self.Current_Enquiry.student_First_Name









