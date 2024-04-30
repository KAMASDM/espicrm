from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import enquiry
from .serializers import EnquirySerializer
from rest_framework.permissions import IsAuthenticated  
from rest_framework_simplejwt.authentication import JWTAuthentication 
class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = enquiry.objects.all()
    serializer_class = EnquirySerializer
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated] 
    
