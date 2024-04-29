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
from Enquiry.views  import EnquiryViewSet
from DetailEnquiry.views  import DetailEnquiryViewSet
from Assessment.views import AssessmentViewSet
from Application.views import ApplicationViewSet
from Accounts.views import PaymentViewSet
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
    PaymentStatusViewSet, PaymentModeViewSet,EnquiryFollowupStatusViewSet, DetailEnquiryFollowupStatusViewSet, AssesmentFollowupStatusViewSet, PaymentFollowupStatusViewSet
)



router = routers.DefaultRouter()
router.register(r'countriesIntersted', CountryInterestedViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'course-levels', CourseLevelsViewSet)
router.register(r'available-services', AvailableServicesViewSet)
router.register(r'current-education', CurrentEducationViewSet)
router.register(r'intakes', IntakeViewSet)
router.register(r'documents-required', DocumentsRequiredViewSet)
router.register(r'course-requirements', CourseRequirementsViewSet)
router.register(r'enquiry-statuses', EnquiryStatusViewSet)
router.register(r'assessment-statuses', AssessmentStatusViewSet)
router.register(r'application-statuses', ApplicationStatusViewSet)
router.register(r'universities', UniversityViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'edu-levels', EduLevelViewSet)
router.register(r'work-experiences', WorkExperienceViewSet)
router.register(r'tenth_std_percentage_requirements', TenthStdPercentageRequirementViewSet)
router.register(r'twelfth_std_percentage_requirements', TwelfthStdPercentageRequirementViewSet)
router.register(r'bachelor_requirements', BachelorRequirementViewSet)
router.register(r'masters_requirements', MastersRequirementViewSet)
router.register(r'rejection_reasons', RejectionReasonViewSet)
router.register(r'detail_enquiry_statuses', DetailEnquiryStatusViewSet)
router.register(r'enquiry_sources', EnquirySourceViewSet)
router.register(r'payment_types', PaymentTypeViewSet)
router.register(r'payment_statuses', PaymentStatusViewSet)
router.register(r'payment_modes', PaymentModeViewSet)
router.register(r'toefl_exams', ToeflExamViewSet)
router.register(r'ielts_exams', IeltsExamViewSet)
router.register(r'pte_exams', PTEExamViewSet)
router.register(r'duolingo_exams', DuolingoExamViewSet)
router.register(r'gre_exams', GreExamViewSet)
router.register(r'gmat_exams', GmatExamViewSet)
router.register(r'enquiries', EnquiryViewSet)
router.register(r'detailsEnquiry',DetailEnquiryViewSet)
router.register(r'assesment',AssessmentViewSet )
router.register(r'application',ApplicationViewSet )
router.register(r'payments', PaymentViewSet)
# router.register(r'followups', FollowupViewSet)
# router.register(r'followups', FollowupViewSet)
# from smart_selects.views import ChainedSelectView
router.register(r'enquiry-followups', EnquiryFollowupStatusViewSet)
router.register(r'detail-enquiry-followups', DetailEnquiryFollowupStatusViewSet)
router.register(r'assessment-followups', AssesmentFollowupStatusViewSet)
router.register(r'payment-followups', PaymentFollowupStatusViewSet)


urlpatterns = [
    # path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('chaining/', include('smart_selects.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair')
   

    # path('admin_charts/', include('admin_charts.urls')),
    ]

