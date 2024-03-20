from django.db import models
from Assessment.models import assessment
from Master.models import application_status
from Enquiry.models import enquiry


# Create your models here.
class Application(models.Model):
    application = models.ForeignKey(assessment, on_delete=models.CASCADE)
    sop = models.FileField(upload_to='sop', blank=True)
    cv = models.FileField(upload_to='cv', blank=True)
    passport = models.FileField(upload_to='passport', blank=True)
    ielts = models.FileField(upload_to='ielts', blank=True)
    gre = models.FileField(upload_to='gre', blank=True)
    toefl = models.FileField(upload_to='toefl', blank=True)
    gmat = models.FileField(upload_to='gmat', blank=True)
    pte = models.FileField(upload_to='pte', blank=True)
    work_experience = models.FileField(upload_to='work_experience', blank=True)
    diploma_marksheet = models.FileField(upload_to='diploma_marksheet', blank=True)
    bachelor_marksheet = models.FileField(upload_to='bachelor_marksheet', blank=True)
    master_marksheet = models.FileField(upload_to='master_marksheet', blank=True)
    other_documents = models.FileField(upload_to='other_documents', blank=True)
    application_status = models.ForeignKey(application_status, max_length=100, blank=True, on_delete=models.CASCADE)



