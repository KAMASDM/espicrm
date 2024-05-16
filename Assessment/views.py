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
    
    
from rest_framework import viewsets
from .models import assessment
from DetailEnquiry.models import *
from Master.models import *
from .serializers import AssessmentSerializer
from rest_framework.permissions import IsAuthenticated  
from rest_framework_simplejwt.authentication import JWTAuthentication 
class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = assessment.objects.all()
    serializer_class = AssessmentSerializer
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated] 
    
    
    


# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AssessmentSerializer
from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.core.serializers import serialize
    


# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AssessmentSerializer
from django.http import Http404

class AssessmentListCreateAPIView(APIView):
    def get(self, request):
        assessments = assessment.objects.all()
        serializer = AssessmentSerializer(assessments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Extract data from request
        data = request.data
        
        # Validate each field individually
        errors = {}
        
        assessment_data = {}

        # Validate assigned_users field
        assigned_users_id = data.get('assigned_users')
        if assigned_users_id is not None:
            try:
                assigned_user = get_user_model().objects.get(id=assigned_users_id)
            except get_user_model().DoesNotExist:
                errors['assigned_users'] = ['Invalid user ID.']
            else:
                assigned_users_data = {
                    'id': assigned_user.id,
                    'username': assigned_user.username,
                    'email': assigned_user.email
                    # Add other fields as needed
                }
        else:
            errors['assigned_users'] = ['This field is required.']

        # Validate other fields
        enquiry_id = data.get('enquiry')
        if enquiry_id is not None:
            try:
                enquiry_obj = Detail_Enquiry.objects.get(id=enquiry_id)
            except Detail_Enquiry.DoesNotExist:
                errors['enquiry'] = ['Invalid enquiry ID.']
            else:
                enquiry_data = {
                    'id': enquiry_obj.id,
                    # Add other fields as needed
                }
        else:
            errors['enquiry'] = ['This field is required.']

        student_country_id = data.get('student_country')
        if student_country_id is not None:
            try:
                student_country = CountryInterested.objects.get(id=student_country_id)
            except CountryInterested.DoesNotExist:
                errors['student_country'] = ['Invalid country ID.']
            else:
                student_country_data = {
                    'id': student_country.id,
                    'country': student_country.country
                    # Add other fields as needed
                }
        else:
            errors['student_country'] = ['This field is required.']
        level_applying_for_id = data.get('level_applying_for')
        if level_applying_for_id is not None:
            try:
                level_applying_for = course_levels.objects.get(id=level_applying_for_id)
            except course_levels.DoesNotExist:
                errors['level_applying_for'] = ['Invalid level ID.']
            else:
                level_applying_for_data = {
                    'id': level_applying_for.id,
                    # Add other fields as needed
                }
        else:
            errors['level_applying_for'] = ['This field is required.']

        # Validate course_interested field
        course_interested_id = data.get('course_interested')
        if course_interested_id is not None:
            try:
                course_interested = Course.objects.get(id=course_interested_id)
            except Course.DoesNotExist:
                errors['course_interested'] = ['Invalid course ID.']
            else:
                course_interested_data = {
                    'id': course_interested.id,
                    # Add other fields as needed
                }
        else:
            errors['course_interested'] = ['This field is required.']

        # Validate intake_interested field
        intake_interested_id = data.get('intake_interested')
        if intake_interested_id is not None:
            try:
                intake_interested = intake.objects.get(id=intake_interested_id)
            except intake.DoesNotExist:
                errors['intake_interested'] = ['Invalid intake ID.']
            else:
                intake_interested_data = {
                    'id': intake_interested.id,
                    # Add other fields as needed
                }
        else:
            errors['intake_interested'] = ['This field is required.']
# Validate AssesmentFollowup field
# Validate AssesmentFollowup field


# Validate AssesmentFollowup field
        # AssesmentFollowup_id = data.get('AssesmentFollowup')
        # if AssesmentFollowup_id is not None:
        #     try:
        #         AssesmentFollowup_obj = AssesmentFollowupStatus.objects.get(id=AssesmentFollowup_id)
        #     except AssesmentFollowupStatus.DoesNotExist:
        #         errors['AssesmentFollowup'] = ['Invalid AssesmentFollowup ID.']
        #     else:
        #         assessment_data['AssesmentFollowup'] = serialize('python', [AssesmentFollowup_obj])[0]['fields']
        # else:
        #     errors['AssesmentFollowup'] = ['This field is required.']


        # Validate ass_status field
        # ass_status_id = data.get('ass_status')
        # if ass_status_id is not None:
        #     try:
        #         ass_status_obj = assessment_status.objects.get(id=ass_status_id)
        #     except assessment_status.DoesNotExist:
        #         errors['ass_status'] = ['Invalid ass_status ID.']
        #     else:
        #         assessment_data['ass_status'] = {
        #             'id': ass_status_obj.id,
        #             'status': ass_status_obj.status  # Assuming 'status' is a field you want to include
        #             # Add other fields as needed
        #         }
        # else:
        #     errors['ass_status'] = ['This field is required.']

            
            
        specialisation = data.get('specialisation')
        if specialisation:
            # Add any additional validation logic here if needed
            assessment_data['specialisation'] = specialisation
            
            
        duration = data.get('duration')
        if duration:
            # Add any additional validation logic here if needed
            assessment_data['duration'] = duration

        application_fee = data.get('application_fee')
        if application_fee:
            # Add any additional validation logic here if needed
            assessment_data['application_fee'] = application_fee

        # Validate tution_fee field
        tution_fee = data.get('tution_fee')
        if tution_fee:
            # Add any additional validation logic here if needed
            assessment_data['tution_fee'] = tution_fee


        fee_currency = data.get('fee_currency')
        if fee_currency:
            # Add any additional validation logic here if needed
            assessment_data['fee_currency'] = fee_currency


        course_link = data.get('course_link')
        if course_link:
            # Add any additional validation logic here if needed
            assessment_data['course_link'] = course_link
            
        notes = data.get('notes')
        if notes:
            # Add any additional validation logic here if needed
            assessment_data['notes'] = notes


        # Combine all data
        if not errors:
            assessment_data = {
                'assigned_users': assigned_users_data,
                'enquiry': enquiry_data,
                'student_country': student_country_data,
                'level_applying_for': level_applying_for_data,
                'course_interested': course_interested_data,
                'intake_interested': intake_interested_data, 
                'specialisation':specialisation,
                'course_link':course_link,
                'fee_currency':fee_currency,
                'application_fee':application_fee,
                # 'AssesmentFollowup':AssesmentFollowup_obj,
                # 'ass_status':ass_status_obj,
                'notes':notes

                

            }
            # Optionally, create the assessment instance here

        # Check for errors
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        # Optionally, return the combined data
        return Response(assessment_data, status=status.HTTP_200_OK)


class AssessmentDetailUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return assessment.objects.get(pk=pk)
        except assessment.DoesNotExist:
            raise 

    def get(self, request, pk):
        assessment = self.get_object(pk)
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)

    def put(self, request, pk):
        assessment = self.get_object(pk)
        serializer = AssessmentSerializer(assessment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        assessment = self.get_object(pk)
        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
