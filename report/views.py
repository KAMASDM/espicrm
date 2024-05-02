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