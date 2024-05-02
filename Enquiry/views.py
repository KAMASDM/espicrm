from rest_framework import viewsets,status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import enquiry
from .serializers import EnquirySerializer, EnquiryCreateSerializerss
from rest_framework.permissions import IsAuthenticated  
from rest_framework_simplejwt.authentication import JWTAuthentication 
class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = enquiry.objects.all()
    serializer_class = EnquirySerializer
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated] 
    

class EnquiryCreateView(generics.ListCreateAPIView):
    queryset = enquiry.objects.all()
    serializer_class = EnquiryCreateSerializerss