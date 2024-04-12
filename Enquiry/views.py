from rest_framework import viewsets, generics
from .models import enquiry
from .serializers import EnquirySerializer, EnquiryCreateSerializerss
# from rest

class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = enquiry.objects.all()
    serializer_class = EnquirySerializer



class EnquiryCreateView(generics.ListCreateAPIView):
    queryset = enquiry.objects.all()
    serializer_class = EnquiryCreateSerializerss