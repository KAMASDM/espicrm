# # Master/schema.py

# import graphene
# from graphene_django import DjangoObjectType
# from .models import course_levels

# class CourseLevelType(DjangoObjectType):
#     class Meta:
#         model = course_levels
#         fields = ("id", "levels")

# class Query(graphene.ObjectType):
#     all_course_levels = graphene.List(CourseLevelType)

#     def resolve_all_course_levels(self, info, **kwargs):
#         # This will return all course level instances
#         return course_levels.objects.all()

# schema = graphene.Schema(query=Query)
import graphene
from graphene_django.types import DjangoObjectType
from .models import (
    country, course_levels, current_education, intake, intake_Year,
    documents_required, course_requirements, enquiry_status, assessment_status,
    application_status, university, Course, Edu_Level, Work_Experience,
    ielts_Exam, Toefl_Exam, PTE_Exam, Duolingo_Exam, Gre_Exam, Gmat_Exam,
    Rejection_Reason
)


class CountryType(DjangoObjectType):
    class Meta:
        model = country


class CourseLevelsType(DjangoObjectType):
    class Meta:
        model = course_levels


class CurrentEducationType(DjangoObjectType):
    class Meta:
        model = current_education


class IntakeType(DjangoObjectType):
    class Meta:
        model = intake


class IntakeYearType(DjangoObjectType):
    class Meta:
        model = intake_Year


class DocumentsRequiredType(DjangoObjectType):
    class Meta:
        model = documents_required


class CourseRequirementsType(DjangoObjectType):
    class Meta:
        model = course_requirements


class EnquiryStatusType(DjangoObjectType):
    class Meta:
        model = enquiry_status


class AssessmentStatusType(DjangoObjectType):
    class Meta:
        model = assessment_status


class ApplicationStatusType(DjangoObjectType):
    class Meta:
        model = application_status


class UniversityType(DjangoObjectType):
    class Meta:
        model = university


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class EduLevelType(DjangoObjectType):
    class Meta:
        model = Edu_Level


class WorkExperienceType(DjangoObjectType):
    class Meta:
        model = Work_Experience


class IeltsExamType(DjangoObjectType):
    class Meta:
        model = ielts_Exam


class ToeflExamType(DjangoObjectType):
    class Meta:
        model = Toefl_Exam


class PteExamType(DjangoObjectType):
    class Meta:
        model = PTE_Exam


class DuolingoExamType(DjangoObjectType):
    class Meta:
        model = Duolingo_Exam


class GreExamType(DjangoObjectType):
    class Meta:
        model = Gre_Exam


class GmatExamType(DjangoObjectType):
    class Meta:
        model = Gmat_Exam


# class RejectionReasonType(DjangoObjectType):
#     class Meta:
#         model = Rejection_Reason


class Query(graphene.ObjectType):
    all_countries = graphene.List(CountryType)
    all_course_levels = graphene.List(CourseLevelsType)
    all_current_educations = graphene.List(CurrentEducationType)
    all_intakes = graphene.List(IntakeType)
    all_intake_years = graphene.List(IntakeYearType)
    all_documents_required = graphene.List(DocumentsRequiredType)
    all_course_requirements = graphene.List(CourseRequirementsType)
    all_enquiry_statuses = graphene.List(EnquiryStatusType)
    all_assessment_statuses = graphene.List(AssessmentStatusType)
    all_application_statuses = graphene.List(ApplicationStatusType)
    all_universities = graphene.List(UniversityType)
    all_courses = graphene.List(CourseType)
    all_edu_levels = graphene.List(EduLevelType)
    all_work_experiences = graphene.List(WorkExperienceType)
    all_ielts_exams = graphene.List(IeltsExamType)
    all_toefl_exams = graphene.List(ToeflExamType)
    all_pte_exams = graphene.List(PteExamType)
    all_duolingo_exams = graphene.List(DuolingoExamType)
    all_gre_exams = graphene.List(GreExamType)
    all_gmat_exams = graphene.List(GmatExamType)
    # all_rejection_reasons = graphene.List(RejectionReasonType)

    def resolve_all_countries(self, info, **kwargs):
            return country.objects.all()

    def resolve_all_course_levels(self, info, **kwargs):
        return course_levels.objects.all()

    def resolve_all_current_educations(self, info, **kwargs):
        return current_education.objects.all()

    def resolve_all_intakes(self, info, **kwargs):
        return intake.objects.all()

    def resolve_all_intake_years(self, info, **kwargs):
        return intake_Year.objects.all()

    def resolve_all_documents_required(self, info, **kwargs):
        return documents_required.objects.all()

    def resolve_all_course_requirements(self, info, **kwargs):
        return course_requirements.objects.all()
    
    def resolve_all_enquiry_statuses(self, info):
        return enquiry_status.objects.all()

    def resolve_all_assessment_statuses(self, info):
        return assessment_status.objects.all()

    def resolve_all_application_statuses(self, info):
        return application_status.objects.all()

    def resolve_all_universities(self, info):
        return university.objects.all()

    def resolve_all_courses(self, info):
        return Course.objects.all()

    def resolve_all_edu_levels(self, info):
        return Edu_Level.objects.all()

    def resolve_all_work_experiences(self, info):
        return Work_Experience.objects.all()

    def resolve_all_ielts_exams(self, info):
        return ielts_Exam.objects.all()

    def resolve_all_toefl_exams(self, info):
        return Toefl_Exam.objects.all()

    def resolve_all_pte_exams(self, info):
        return PTE_Exam.objects.all()

    def resolve_all_duolingo_exams(self, info):
        return Duolingo_Exam.objects.all()

    def resolve_all_gre_exams(self, info):
        return Gre_Exam.objects.all()

    def resolve_all_gmat_exams(self, info):
        return Gmat_Exam.objects.all()

    # def resolve_all_rejection_reasons(self, info):
    #     return Rejection_Reason.objects.all()


schema = graphene.Schema(query=Query)                                                                                                                                                                                                                                                                                     
