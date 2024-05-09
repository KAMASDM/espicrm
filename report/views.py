from django.shortcuts import render
from django.db import models
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from Enquiry.models import enquiry
from Application.models import Application
from Assessment.models import assessment
from DetailEnquiry.models import * 
from Master.models import Enquiry_Source,CountryInterested,course_levels

class EnquirySummaryReport(APIView):
    def get(self, request):
        # Get counts of enquiries by source, country, and course level
        source_counts = enquiry.objects.values('Source_Enquiry__Source').annotate(count=models.Count('id'))
        country_counts = enquiry.objects.values('country_interested__country').annotate(count=models.Count('id'))
        course_level_counts = enquiry.objects.values('level_applying_for__levels').annotate(count=models.Count('id'))

        # Format data
        summary_data = {
            'source_counts': [{'source': item['Source_Enquiry__Source'], 'count': item['count']} for item in source_counts],
            'country_counts': [{'country': item['country_interested__country'], 'count': item['count']} for item in country_counts],
            'course_level_counts': [{'course_level': item['level_applying_for__levels'], 'count': item['count']} for item in course_level_counts],
        }
        return Response(summary_data)


class LeadConversionReport(APIView):
    def get(self, request):
        # Calculate lead conversion rate
        total_enquiries = enquiry.objects.count()
        total_applications = Application.objects.count()
        conversion_rate = (total_applications / total_enquiries) * 100 if total_enquiries != 0 else 0

        # Fetch more data or perform additional calculations as needed

        # Format data
        report_data = {
            'total_enquiries': total_enquiries,
            'total_applications': total_applications,
            'conversion_rate': conversion_rate,
            # Add more data as needed
        }
        return Response(report_data)


class RegionWiseEnquiryReport(APIView):
    def get(self, request):
        # Get counts of enquiries by region/country
        region_counts = enquiry.objects.values('country_interested__country').annotate(count=models.Count('id'))

        # Format data
        report_data = {item['country_interested__country']: item['count'] for item in region_counts}
        return Response(report_data)

from rest_framework.response import Response
from Assessment.models import assessment
from Master.models import *


class ApplicationStatusReport(APIView):
    def get(self, request, format=None):
        # Retrieve all applications with their current status and rejection reasons
        applications = Application.objects.select_related('application_status').all()
        
        # Define a list to store the report data
        report = []
        
        # Iterate over each application and populate the report
        for app in applications:
            report.append({
                'application_id': app.id,
                'application_status': app.application_status.App_status,
                'rejection_reason': app.Rejection_reason if app.application_status.App_status == 'Rejected' else None
            })
        
        # Return the report as a JSON response
        return Response(report)



class AssessmentOverviewReport(APIView):
    def get(self, request, format=None):
        assessments = assessment.objects.select_related('ass_status').all()
        report = {}
        for assess in assessments:
            status_name = assess.ass_status
            if status_name not in report:
                report[status_name] = 0
            report[status_name] += 1
        return Response(report)


class UniversityCoursePopularityReport(APIView):
    def get(self, request, format=None):
        universities = university.objects.annotate(num_applications=models.Count('assessment')).order_by('-num_applications')
        courses = Course.objects.annotate(num_applications=models.Count('assessment')).order_by('-num_applications')
        university_report = [{'university': uni.univ_name, 'num_applications': uni.num_applications} for uni in universities]
        course_report = [{'course': course.course_name, 'num_applications': course.num_applications} for course in courses]
        return Response({'universities': university_report,'courses': course_report})
    
    
    


class CampaignPerformanceReport(APIView):
    def get(self, request, format=None):
        # Perform analysis of marketing campaigns based on the source of enquiries and applications
        source_enquiries = enquiry.objects.values('Source_Enquiry__Source').annotate(enquiry_count=models.Count('id'))
        source_applications = Application.objects.values('application_id').annotate(application_count=models.Count('id'))
        #print(source_applications)
        # Combine the results
        campaign_performance = {}
        for enquiry_source in source_enquiries:
            source_name = enquiry_source['Source_Enquiry__Source']
            campaign_performance[source_name] = {
                'enquiry_count': enquiry_source['enquiry_count'],
                'application_count': source_applications[1]
            }
        
        for application_source in source_applications:
            source_name = application_source['application_id']
            if source_name in campaign_performance:
                campaign_performance[source_name]['Source_Enquiry__Source'] = application_source['application_count']
        
        return Response(campaign_performance)


class EngagementAnalysisReport(APIView):
    def get(self, request, format=None):
        # Get count of enquiries, applications, and follow-up statuses
        total_enquiries = enquiry.objects.count()
        total_applications = Application.objects.count()
        follow_up_statuses = enquiry.objects.values('EnquiryFollowup').annotate(count=models.Count('EnquiryFollowup'))
        
        # Calculate total interactions
        total_interactions = total_enquiries + total_applications
        
        # Return engagement analysis report
        report = {
            'total_enquiries': total_enquiries,
            'total_applications': total_applications,
            'total_interactions': total_interactions,
            'follow_up_statuses': follow_up_statuses
        }
        return Response(report)
    
class InterestAnalysisReport(APIView):
    def get(self, request, format=None):
        # Get trends in course interests, preferred countries, and levels of study
        course_interests = enquiry.objects.values('course_interested__course_name').annotate(count=models.Count('course_interested'))
        preferred_countries = enquiry.objects.values('country_interested__country').annotate(count=models.Count('student_country'))
        levels_of_study = enquiry.objects.values('level_applying_for__levels').annotate(count=models.Count('level_applying_for'))
        
        # Return interest analysis report
        report = {
            'course_interests': course_interests,
            'preferred_countries': preferred_countries,
            'levels_of_study': levels_of_study
        }
        return Response(report)
    
    
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Payment
# from Accounts.serializers import PaymentSerializer

# class PaymentTrackingReport(APIView):
#     def get(self, request, format=None):
#         payments = Payment.objects.all()
#         serializer = PaymentSerializer(payments, many=True)
#         return Response(serializer.data)

# class RevenueAnalysisReport(APIView):
#     def get(self, request, format=None):
#         # Perform revenue analysis calculations
#         # Example: Calculate total revenue from payments
#         total_revenue = Payment.objects.aggregate(total=models.Sum('payment_amount'))['total']
#         return Response({'total_revenue': total_revenue})

# class ScholarshipFundingReport(APIView):
#     def get(self, request, format=None):
#         # Query payments related to scholarships or funding
#         scholarship_payments = Payment.objects.filter(Payment_For__name='Scholarship')
#         serializer = PaymentSerializer(scholarship_payments, many=True)
#         return Response(serializer.data)



from DetailEnquiry.serializers import DetailEnquirySerializer

class StandardizedTestScoresReportAPIView(APIView):
    def get(self, request):
        # Query standardized test scores data
        test_scores_data = Detail_Enquiry.objects.all().values(
            'Current_Enquiry__student_First_Name',
            'ielts_Exam__Overall',  # Example field for IELTS score
            'Toefl_Exam__Overall',  # Example field for TOEFL score
            'PTE_Exam__Overall', # Example field for PTE
            'Duolingo_Exam__Overall', # Example field for Duolingo_Exam
            'Gre_Exam__Overall', # Example field for Gre
            'Gmat_Exam__Overall', # Example field for Gmat
            
            # Add more fields for other test scores as needed
        )
        return Response(test_scores_data)

# class EducationBackgroundReportAPIView(APIView):
#     def get(self, request):
#         # Query education background data
#         education_background_data = Detail_Enquiry.objects.all().values(
#             'id',
#             'Current_Education_Details__level',  # Example field for current education level
#             'Work_Experience__Designation',  # Example field for work experience
#             # Add more fields for other education background information as needed
#         )
#         return Response(education_background_data)

# from datetime import datetime

# class EducationBackgroundReportAPIView(APIView):
#     def get(self, request):
#         # Query education background data
#         education_background_data = Detail_Enquiry.objects.all().values(
#             'id',
#             'Current_Education_Details__level',
#             'Work_Experience__Designation',  # Example field for work experience
#             # Add more fields for other education background information as needed
#         )

        # Calculate total years of experience for each record
    #     for data in education_background_data:
    #         work_experience_id = data['Work_Experience']
    #         if work_experience_id:
    #             work_experience = Work_Experience.objects.get(pk=work_experience_id)
    #             start_date = work_experience.Start_Date
    #             end_date = work_experience.End_Date
    #             if start_date and end_date:
    #                 # Calculate total years of experience
    #                 total_experience_years = self.calculate_experience_years(start_date, end_date)
    #                 data['total_experience_years'] = total_experience_years
    #             else:
    #                 data['total_experience_years'] = None
    #         else:
    #             data['total_experience_years'] = None

    #     return Response(education_background_data)

    # def calculate_experience_years(self, start_date, end_date):
    #     # Calculate total years of experience
    #     total_experience_years = (end_date - start_date).days / 365.25
    #     return round(total_experience_years, 1)

from datetime import datetime

class EducationBackgroundReportAPIView(APIView):
    def get(self, request):
        # Query education background data
        education_background_data = Detail_Enquiry.objects.all().values(
            'id',
            'Current_Education_Details__level',
            'Graduation_Education_Details__level',
            'Twelveth_Education_Details__level',
            'Tenth_Education_Details__level',
            # Example field for current education level
            'Work_Experience__Designation',  # Example field for work experience
            # Add more fields for other education background information as needed
        )

        # Calculate total years of experience for each record
        for data in education_background_data:
            work_experience_designation = data['Work_Experience__Designation']
            if work_experience_designation:
                total_experience_years = self.calculate_total_experience_years(work_experience_designation)
                data['total_experience_years'] = total_experience_years
            else:
                data['total_experience_years'] = None

        return Response(education_background_data)

    def calculate_total_experience_years(self, designation):
        # Query work experiences for the given designation
        work_experiences = Work_Experience.objects.filter(Designation=designation)
        
        total_experience_years = 0
        for experience in work_experiences:
            start_date = experience.Start_Date
            end_date = experience.End_Date
            
            # Calculate the difference between end date and start date
            duration = (end_date - start_date).days
            
            # Convert days to years (assuming 365.25 days per year to account for leap years)
            years = duration / 365.25
            
            total_experience_years = years
        
        return round(total_experience_years, 1)  # Round to two decimal places




from django.contrib.auth.models import User
from user.models import CustomUser

class UserActivityReport(APIView):
    def get(self, request):
        # Query to count login frequency
        login_frequency = CustomUser.objects.annotate(login_count=models.Count('last_login')).values('username', 'login_count')

        # Query to find most accessed services
        # Assuming there's a field in the User model linking to accessed services

        # Query to track feature usage
        # Assuming there's a field in the User model tracking feature usage

        return Response({
            'login_frequency': login_frequency,
            # Add data for most accessed services and feature usage
        })

class ServiceRequestReport(APIView):
    def get(self, request):
        # Query to get details on enquiries and follow-up status
        service_requests = enquiry.objects.all().values(
            'id',
            'student_First_Name',
            'EnquiryFollowup__status',  # Assuming this field tracks follow-up status
            # Add more fields as needed for response times and pending actions
        )

        return Response(service_requests)
from Accounts.models import Payment
from Accounts.serializers import PaymentSerializer
from django.db.models import Sum

class PaymentTrackingReportAPIView(APIView):
    def get(self, request):
        # Query all payments
        payments = Payment.objects.all()
        
        # Serialize payments
        serializer = PaymentSerializer(payments, many=True)
        
        return Response(serializer.data)

class RevenueAnalysisReportAPIView(APIView):
    def get(self, request):
        # Get the ID of the 'success' status
        success_status_id = Payment_Status.objects.get(Status='success').id
        
        # Query successful payments
        successful_payments = Payment.objects.filter(payment_status_id=success_status_id)
        
        # Aggregate revenue
        total_revenue = successful_payments.aggregate(total=Sum('payment_amount'))['total']
        
        
        revenue_by_course = successful_payments.values('Payment_For__Services').annotate(total_revenue=Sum('payment_amount'))
        revenue_by_university = successful_payments.values('Payment_For__Interested_Services').annotate(total_revenue=Sum('payment_amount'))
        
        return Response({
            'total_revenue_all': total_revenue,
            'revenue_by_course': revenue_by_course,
            'revenue_by_university': revenue_by_university,
        })
        


class ScholarshipFundingReportAPIView(APIView):
    def get(self, request):
        # Query payments related to scholarships and funding
        scholarship_payments = Payment_Type.objects.filter(Type='Scholarship')
        funding_payments = Payment_Type.objects.filter(Type='Funding')
        
        # Serialize scholarship_payments and funding_payments
        scholarship_serializer = PaymentSerializer(scholarship_payments, many=True)
        funding_serializer = PaymentSerializer(funding_payments, many=True)
        
        return Response({
            'scholarship_payments': scholarship_serializer.data,
            'funding_payments': funding_serializer.data
        })
