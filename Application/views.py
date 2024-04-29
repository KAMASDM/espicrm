from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated  
from rest_framework_simplejwt.authentication import JWTAuthentication 

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated] 
