from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,status
from .models import assessment
from .serializers import AssessmentSerializer
from rest_framework.response import Response

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = assessment.objects.all()
    serializer_class = AssessmentSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Success: 201 Created
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Failure: 400 Bad Request

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)  # Success: 200 OK

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)  # Success: 200 OK
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Failure: 400 Bad Request

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)  # Success: 204 No Content
