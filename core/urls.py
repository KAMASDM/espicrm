"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from graphene_django.views import GraphQLView
from rest_framework_simplejwt.views import TokenObtainPairView
from Master.schema import schema
from rest_framework import routers
from Enquiry.views  import EnquiryViewSet, EnquiryCreateView
from DetailEnquiry.views  import DetailEnquiryViewSet
from Assessment.views import AssessmentViewSet
from Application.views import ApplicationViewSet
from Accounts.views import PaymentViewSet
from report.views import (EnquirySummaryReport, LeadConversionReport, RegionWiseEnquiryReport,InterestAnalysisReport,
                          EngagementAnalysisReport,CampaignPerformanceReport,UniversityCoursePopularityReport,
                          ApplicationStatusReport,AssessmentOverviewReport,StandardizedTestScoresReportAPIView,
                          EducationBackgroundReportAPIView,UserActivityReport,ServiceRequestReport
                          )
from Master.views import (
    CountryInterestedViewSet,
    CountryViewSet, CourseLevelsViewSet, AvailableServicesViewSet,
    CurrentEducationViewSet, IntakeViewSet, DocumentsRequiredViewSet,
    CourseRequirementsViewSet, EnquiryStatusViewSet, AssessmentStatusViewSet,
    ApplicationStatusViewSet, UniversityViewSet, CourseViewSet, EduLevelViewSet,
    WorkExperienceViewSet, IeltsExamViewSet, ToeflExamViewSet, PTEExamViewSet,
    DuolingoExamViewSet, GreExamViewSet, GmatExamViewSet,
    TenthStdPercentageRequirementViewSet, TwelfthStdPercentageRequirementViewSet,
    BachelorRequirementViewSet, MastersRequirementViewSet, RejectionReasonViewSet,
    DetailEnquiryStatusViewSet, EnquirySourceViewSet, PaymentTypeViewSet,
    PaymentStatusViewSet, PaymentModeViewSet,
    # FollowupViewSet
    PaymentStatusViewSet, PaymentModeViewSet,EnquiryFollowupStatusViewSet, DetailEnquiryFollowupStatusViewSet,
AssesmentFollowupStatusViewSet, PaymentFollowupStatusViewSet,
)
from user.views import CustomUserViewSet


router = routers.DefaultRouter()
router.register('countriesIntersted', CountryInterestedViewSet)
router.register('countries', CountryViewSet)
router.register('course-levels', CourseLevelsViewSet)
router.register('available-services', AvailableServicesViewSet)
router.register('current-education', CurrentEducationViewSet)
router.register('intakes', IntakeViewSet)
router.register('documents-required', DocumentsRequiredViewSet)
router.register('course-requirements', CourseRequirementsViewSet)
router.register('enquiry-statuses', EnquiryStatusViewSet)
router.register('assessment-statuses', AssessmentStatusViewSet)
router.register('application-statuses', ApplicationStatusViewSet)
router.register('universities', UniversityViewSet)
router.register('courses', CourseViewSet)
router.register('edu-levels', EduLevelViewSet)
router.register('work-experiences', WorkExperienceViewSet)
router.register('tenth_std_percentage_requirements', TenthStdPercentageRequirementViewSet)
router.register('twelfth_std_percentage_requirements', TwelfthStdPercentageRequirementViewSet)
router.register('bachelor_requirements', BachelorRequirementViewSet)
router.register('masters_requirements', MastersRequirementViewSet)
router.register('rejection_reasons', RejectionReasonViewSet)
router.register('detail_enquiry_statuses', DetailEnquiryStatusViewSet)
router.register('enquiry_sources', EnquirySourceViewSet)
router.register('payment_types', PaymentTypeViewSet)
router.register('payment_statuses', PaymentStatusViewSet)
router.register('payment_modes', PaymentModeViewSet)
router.register('toefl_exams', ToeflExamViewSet)
router.register('ielts_exams', IeltsExamViewSet)
router.register('pte_exams', PTEExamViewSet)
router.register('duolingo_exams', DuolingoExamViewSet)
router.register('gre_exams', GreExamViewSet)
router.register('gmat_exams', GmatExamViewSet)
router.register('enquiries', EnquiryViewSet)
router.register('detailsEnquiry',DetailEnquiryViewSet)
router.register('assesment',AssessmentViewSet )
router.register('application',ApplicationViewSet )
router.register('payments', PaymentViewSet)
# router.register(r'followups', FollowupViewSet)
# router.register(r'followups', FollowupViewSet)
# from smart_selects.views import ChainedSelectView
router.register('enquiry-followups', EnquiryFollowupStatusViewSet)
router.register('detail-enquiry-followups', DetailEnquiryFollowupStatusViewSet)
router.register('assessment-followups', AssesmentFollowupStatusViewSet)
router.register('payment-followups', PaymentFollowupStatusViewSet)
router.register('users', CustomUserViewSet)


urlpatterns = [
    # path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('chaining/', include('smart_selects.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('enquiry-summaryreport/', EnquirySummaryReport.as_view(), name='enquiry_summary'),
    path('lead-conversionreport/', LeadConversionReport.as_view(), name='lead_conversion'),
    path('region-wise-enquiryreport/', RegionWiseEnquiryReport.as_view(), name='region_wise_enquiry'),
    path('api/create-enquiry/', EnquiryCreateView.as_view(), name='create-enquiry'),
    #Admission and Application Reports
    path('api/application-status/', ApplicationStatusReport.as_view(), name='application-status'),
    path('api/assessment-overview/', AssessmentOverviewReport.as_view(), name='assessment-overview'),
    path('api/university-course-popularity/', UniversityCoursePopularityReport.as_view(), name='university-course-popularity'),
    #CampaignPerformanceReport
    path('api/campaign-performance/', CampaignPerformanceReport.as_view(), name='campaign_performance_report'),
    path('api/engagement-analysis/', EngagementAnalysisReport.as_view(), name='engagement-analysis'),
    path('api/interest-analysis/', InterestAnalysisReport.as_view(), name='interest-analysis'),
    #Academic Performance Reports
    path('standardized-test-scores/', StandardizedTestScoresReportAPIView.as_view(), name='standardized-test-scores-report'),
    path('education-background/', EducationBackgroundReportAPIView.as_view(), name='education-background-report'),
    #Customer Service Reports
    path('user-activity/', UserActivityReport.as_view(), name='user_activity_report'),
    path('service-request/', ServiceRequestReport.as_view(), name='service_request_report'),

    # path('admin_charts/', include('admin_charts.urls')),
    ]

