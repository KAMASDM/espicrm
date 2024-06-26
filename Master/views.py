from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets
from .models import (
    CountryInterested,
    country, course_levels, Available_Services, current_education,
    intake, documents_required, course_requirements, enquiry_status,
    assessment_status, application_status, university, Course,
    Edu_Level, Work_Experience, Ielts_Exam, Toefl_Exam, PTE_Exam,
    Duolingo_Exam, Gre_Exam, Gmat_Exam, tenth_std_percentage_requirement,
    twelfth_std_percentage_requirement, bachelor_requirement, masters_requirement,
    Rejection_Reason, Detail_Enquiry_Status, Enquiry_Source,
    Payment_Type, Payment_Status, Payment_Mode,EnquiryFollowupStatus, DetailEnquiryFollowupStatus, AssesmentFollowupStatus, PaymentFollowupStatus
)
from .serializers import (
    CountryInterestedSerializer,
    CountrySerializer, CourseLevelsSerializer, AvailableServicesSerializer,
    CurrentEducationSerializer, IntakeSerializer, DocumentsRequiredSerializer,
    CourseRequirementsSerializer, EnquiryStatusSerializer, AssessmentStatusSerializer,
    ApplicationStatusSerializer, UniversitySerializer, CourseSerializer,
    EduLevelSerializer, WorkExperienceSerializer, IeltsExamSerializer,
    ToeflExamSerializer, PTEExamSerializer, DuolingoExamSerializer,
    GreExamSerializer, GmatExamSerializer, TenthStdPercentageRequirementSerializer,
    TwelfthStdPercentageRequirementSerializer, BachelorRequirementSerializer,
    MastersRequirementSerializer, RejectionReasonSerializer, DetailEnquiryStatusSerializer,
    EnquirySourceSerializer, PaymentTypeSerializer, PaymentStatusSerializer,
    PaymentModeSerializer,EnquiryFollowupStatusSerializer, DetailEnquiryFollowupStatusSerializer, AssesmentFollowupStatusSerializer, PaymentFollowupStatusSerializer
)
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticated permission
from rest_framework_simplejwt.authentication import JWTAuthentication
class CountryInterestedViewSet(viewsets.ModelViewSet):
    queryset = CountryInterested.objects.all()
    serializer_class = CountryInterestedSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = country.objects.all()
    serializer_class = CountrySerializer

class CourseLevelsViewSet(viewsets.ModelViewSet):
    queryset = course_levels.objects.all()
    serializer_class = CourseLevelsSerializer

class AvailableServicesViewSet(viewsets.ModelViewSet):
    queryset = Available_Services.objects.all()
    serializer_class = AvailableServicesSerializer
class CurrentEducationViewSet(viewsets.ModelViewSet):
    queryset = current_education.objects.all()
    serializer_class = CurrentEducationSerializer

class IntakeViewSet(viewsets.ModelViewSet):
    queryset = intake.objects.all()
    serializer_class = IntakeSerializer

class DocumentsRequiredViewSet(viewsets.ModelViewSet):
    queryset = documents_required.objects.all()
    serializer_class = DocumentsRequiredSerializer
    
class CourseRequirementsViewSet(viewsets.ModelViewSet):
    queryset = course_requirements.objects.all()
    serializer_class = CourseRequirementsSerializer

class EnquiryStatusViewSet(viewsets.ModelViewSet):
    queryset = enquiry_status.objects.all()
    serializer_class = EnquiryStatusSerializer

class AssessmentStatusViewSet(viewsets.ModelViewSet):
    queryset = assessment_status.objects.all()
    serializer_class = AssessmentStatusSerializer

class ApplicationStatusViewSet(viewsets.ModelViewSet):
    queryset = application_status.objects.all()
    serializer_class = ApplicationStatusSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = university.objects.all()
    serializer_class = UniversitySerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EduLevelViewSet(viewsets.ModelViewSet):
    queryset = Edu_Level.objects.all()
    serializer_class = EduLevelSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = Work_Experience.objects.all()
    serializer_class = WorkExperienceSerializer
    
class TenthStdPercentageRequirementViewSet(viewsets.ModelViewSet):
    queryset = tenth_std_percentage_requirement.objects.all()
    serializer_class = TenthStdPercentageRequirementSerializer

class TwelfthStdPercentageRequirementViewSet(viewsets.ModelViewSet):
    queryset = twelfth_std_percentage_requirement.objects.all()
    serializer_class = TwelfthStdPercentageRequirementSerializer

class BachelorRequirementViewSet(viewsets.ModelViewSet):
    queryset = bachelor_requirement.objects.all()
    serializer_class = BachelorRequirementSerializer

class MastersRequirementViewSet(viewsets.ModelViewSet):
    queryset = masters_requirement.objects.all()
    serializer_class = MastersRequirementSerializer

class RejectionReasonViewSet(viewsets.ModelViewSet):
    queryset = Rejection_Reason.objects.all()
    serializer_class = RejectionReasonSerializer

class DetailEnquiryStatusViewSet(viewsets.ModelViewSet):
    queryset = Detail_Enquiry_Status.objects.all()
    serializer_class = DetailEnquiryStatusSerializer

class EnquirySourceViewSet(viewsets.ModelViewSet):
    queryset = Enquiry_Source.objects.all()
    serializer_class = EnquirySourceSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = Payment_Type.objects.all()
    serializer_class = PaymentTypeSerializer

class PaymentStatusViewSet(viewsets.ModelViewSet):
    queryset = Payment_Status.objects.all()
    serializer_class = PaymentStatusSerializer

class PaymentModeViewSet(viewsets.ModelViewSet):
    queryset = Payment_Mode.objects.all()
    serializer_class = PaymentModeSerializer

class ToeflExamViewSet(viewsets.ModelViewSet):
    queryset = Toefl_Exam.objects.all()
    serializer_class = ToeflExamSerializer

class IeltsExamViewSet(viewsets.ModelViewSet):
    queryset = Ielts_Exam.objects.all()
    serializer_class = IeltsExamSerializer

class PTEExamViewSet(viewsets.ModelViewSet):
    queryset = PTE_Exam.objects.all()
    serializer_class = PTEExamSerializer

class DuolingoExamViewSet(viewsets.ModelViewSet):
    queryset = Duolingo_Exam.objects.all()
    serializer_class = DuolingoExamSerializer

class GreExamViewSet(viewsets.ModelViewSet):
    queryset = Gre_Exam.objects.all()
    serializer_class = GreExamSerializer

class GmatExamViewSet(viewsets.ModelViewSet):
    queryset = Gmat_Exam.objects.all()
    serializer_class = GmatExamSerializer
    

# class FollowupViewSet(viewsets.ModelViewSet):
#     queryset = Followup.objects.all()
#     serializer_class = FollowupSerializer


class EnquiryFollowupStatusViewSet(viewsets.ModelViewSet):
    queryset = EnquiryFollowupStatus.objects.all()
    serializer_class = EnquiryFollowupStatusSerializer
    authentication_classes = [JWTAuthentication]  # Add JWTAuthentication
    permission_classes = [IsAuthenticated] 
    
    def perform_create(self, serializer):
            serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        user_id = request.query_params.get('user', None)
        if user_id is not None:
            queryset = self.queryset.filter(user_id=user_id)
        else:
            queryset = self.queryset.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class DetailEnquiryFollowupStatusViewSet(viewsets.ModelViewSet):
    queryset = DetailEnquiryFollowupStatus.objects.all()
    serializer_class = DetailEnquiryFollowupStatusSerializer
    authentication_classes = [JWTAuthentication]  # Add JWTAuthentication
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
            serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        user_id = request.query_params.get('user', None)
        if user_id is not None:
            queryset = self.queryset.filter(user_id=user_id)
        else:
            queryset = self.queryset.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AssesmentFollowupStatusViewSet(viewsets.ModelViewSet):
    queryset = AssesmentFollowupStatus.objects.all()
    serializer_class = AssesmentFollowupStatusSerializer
    authentication_classes = [JWTAuthentication]  # Add JWTAuthentication
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
            serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        user_id = request.query_params.get('user', None)
        if user_id is not None:
            queryset = self.queryset.filter(user_id=user_id)
        else:
            queryset = self.queryset.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class PaymentFollowupStatusViewSet(viewsets.ModelViewSet):
    queryset = PaymentFollowupStatus.objects.all()
    serializer_class = PaymentFollowupStatusSerializer
    authentication_classes = [JWTAuthentication]  # Add JWTAuthentication
    permission_classes = [IsAuthenticated] 
    
    def perform_create(self, serializer):
            serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        user_id = request.query_params.get('user', None)
        if user_id is not None:
            queryset = self.queryset.filter(user_id=user_id)
        else:
            queryset = self.queryset.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
