from django.shortcuts import render
from django.db import models
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from Enquiry.models import enquiry
from Application.models import Application  # Import your models here
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
