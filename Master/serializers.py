from rest_framework import serializers
from .models import (CountryInterested,
    country, course_levels, Available_Services, current_education,
    intake, documents_required, course_requirements, enquiry_status,
    assessment_status, application_status, university, Course,
    Edu_Level, Work_Experience, Ielts_Exam, Toefl_Exam, PTE_Exam,
    Duolingo_Exam, Gre_Exam, Gmat_Exam, tenth_std_percentage_requirement,
    twelfth_std_percentage_requirement, bachelor_requirement, masters_requirement,
    Rejection_Reason, Detail_Enquiry_Status, Enquiry_Source,
    Payment_Type, Payment_Status, Payment_Mode
)
class CountryInterestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryInterested
        fields = '__all__'
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = country
        fields = '__all__'

class CourseLevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_levels
        fields = '__all__'

class AvailableServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Available_Services
        fields = '__all__'

class CurrentEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = current_education
        fields = '__all__'

class IntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = intake
        fields = '__all__'

class DocumentsRequiredSerializer(serializers.ModelSerializer):
    class Meta:
        model = documents_required
        fields = '__all__'

class CourseRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_requirements
        fields = '__all__'

class EnquiryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = enquiry_status
        fields = '__all__'

class AssessmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = assessment_status
        fields = '__all__'

class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = application_status
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = university
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EduLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edu_Level
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_Experience
        fields = '__all__'

class IeltsExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ielts_Exam
        fields = '__all__'

class ToeflExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toefl_Exam
        fields = '__all__'

class PTEExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PTE_Exam
        fields = '__all__'

class DuolingoExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duolingo_Exam
        fields = '__all__'

class GreExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gre_Exam
        fields = '__all__'

class GmatExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gmat_Exam
        fields = '__all__'

class TenthStdPercentageRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = tenth_std_percentage_requirement
        fields = '__all__'

class TwelfthStdPercentageRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = twelfth_std_percentage_requirement
        fields = '__all__'

class BachelorRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = bachelor_requirement
        fields = '__all__'

class MastersRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = masters_requirement
        fields = '__all__'

class RejectionReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rejection_Reason
        fields = '__all__'

class DetailEnquiryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail_Enquiry_Status
        fields = '__all__'

class EnquirySourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry_Source
        fields = '__all__'

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Type
        fields = '__all__'

class PaymentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Status
        fields = '__all__'

class PaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Mode
        fields = '__all__'

from rest_framework import serializers
# from .models import Followup

# class FollowupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Followup
#         fields = '__all__'
