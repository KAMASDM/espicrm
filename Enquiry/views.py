from rest_framework import viewsets
from .models import enquiry
from .serializers import EnquirySerializer
from rest_framework.response import Response
import requests

from django.db.models.signals import post_save
from django.dispatch import receiver
from Enquiry.models import enquiry

# Import the necessary modules for sending notifications
import requests

class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = enquiry.objects.all()
    serializer_class = EnquirySerializer