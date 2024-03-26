from django.db import models

# Create your models here.
from Enquiry.models import enquiry
from Master.models import Edu_Level, Work_Experience, Toefl_Exam, ielts_Exam, PTE_Exam, Duolingo_Exam, Gre_Exam, Gmat_Exam, Rejection_Reason

class Detail_Enquiry(models.Model):

    Current_Enquiry = models.ForeignKey(enquiry, on_delete=models.CASCADE)
    level = models.ForeignKey(Edu_Level, on_delete=models.CASCADE)
    work_experience = models.ForeignKey(Work_Experience, on_delete=models.CASCADE)
    toefl_exam = models.ForeignKey(Toefl_Exam, on_delete=models.CASCADE)
    ielts_exam = models.ForeignKey(ielts_Exam, on_delete=models.CASCADE)
    PTE_exam = models.ForeignKey(PTE_Exam, on_delete=models.CASCADE)
    duolingo_exam = models.ForeignKey(Duolingo_Exam, on_delete=models.CASCADE)
    Gre_exam = models.ForeignKey(Gre_Exam, on_delete=models.CASCADE, related_name="gre_exam")
    Gmat_exam = models.ForeignKey(Gmat_Exam, on_delete=models.CASCADE, related_name="gmat_exam")
    Father_occupation = models.CharField(max_length=100)
    Father_annual_Income = models.FloatField()
    Refusal = models.ForeignKey(Rejection_Reason, on_delete=models.CASCADE,null=True)
    Twelveth_document = models.FileField(upload_to='documents/')
    Tenth_document = models.FileField(upload_to='documents/')
    Graduation_marksheet = models.FileField(upload_to='documents/')
    Graduation_certificate = models.FileField(upload_to='documents/')

    UG_marksheet = models.FileField(upload_to='documents/')
    UG_certificate = models.FileField(upload_to='documents/')

    Work_Experience_document = models.FileField(upload_to='documents/')
    Passport_Document = models.FileField(upload_to='documents/')
    Offer_Letter = models.FileField(upload_to='documents/')
    Ielts_Result = models.FileField(upload_to='documents/')
    Toefl_Result = models.FileField(upload_to='documents/')
    PTE_Result = models.FileField(upload_to='documents/')
    Duolingo_Result = models.FileField(upload_to='documents/')
    Gre_Result = models.FileField(upload_to='documents/')
    Gmat_Result = models.FileField(upload_to='documents/')
    level = models.ForeignKey(Edu_Level, on_delete=models.CASCADE, blank=True, null=True)
    work_experience = models.ForeignKey(Work_Experience, on_delete=models.CASCADE, blank=True, null=True)
    toefl_exam = models.ForeignKey(Toefl_Exam, on_delete=models.CASCADE, blank=True, null=True)
    ielts_exam = models.ForeignKey(ielts_Exam, on_delete=models.CASCADE, blank=True, null=True)
    PTE_exam = models.ForeignKey(PTE_Exam, on_delete=models.CASCADE, blank=True, null=True)
    duolingo_exam = models.ForeignKey(Duolingo_Exam, on_delete=models.CASCADE, blank=True, null=True)
    Gre_Exam = models.ForeignKey(Gre_Exam, on_delete=models.CASCADE, blank=True, null=True)
    Gmat_Exam = models.ForeignKey(Gmat_Exam, on_delete=models.CASCADE, blank=True, null=True)
    Father_Occupation = models.CharField(max_length=100, blank=True, null=True)
    Father_Annual_Income = models.FloatField(blank=True, null=True)
    Refusal = models.ForeignKey(Rejection_Reason, on_delete=models.CASCADE, blank=True, null=True)
    Twelveth_Document = models.FileField(upload_to='documents/', blank=True)
    Tenth_Document = models.FileField(upload_to='documents/', blank=True)
    Graduation_Marksheet = models.FileField(upload_to='documents/', blank=True)
    Graduation_Certificate = models.FileField(upload_to='documents/', blank=True)
    UG_Marksheet = models.FileField(upload_to='documents/', blank=True)
    UG_Certificate = models.FileField(upload_to='documents/', blank=True)
    Work_Experience_Document = models.FileField(upload_to='documents/', blank=True)
    Passport_Document = models.FileField(upload_to='documents/', blank=True)
    Offer_Letter = models.FileField(upload_to='documents/', blank=True)
    Ielts_Result = models.FileField(upload_to='documents/', blank=True)
    Toefl_Result = models.FileField(upload_to='documents/', blank=True)
    PTE_Result = models.FileField(upload_to='documents/', blank=True)
    Duolingo_Result = models.FileField(upload_to='documents/', blank=True)
    Gre_Result = models.FileField(upload_to='documents/', blank=True)
    Gmat_Result = models.FileField(upload_to='documents/', blank=True)
    def __str__(self):
        return self.Current_Enquiry









