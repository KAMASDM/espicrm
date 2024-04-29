from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import assessment
from .serializers import AssessmentSerializer
from rest_framework.permissions import IsAuthenticated  
from rest_framework_simplejwt.authentication import JWTAuthentication 
class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = assessment.objects.all()
    serializer_class = AssessmentSerializer
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated] 
    
