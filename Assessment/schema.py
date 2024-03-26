import graphene
from graphene_django.types import DjangoObjectType
from .models import assessment


class AssessmentType(DjangoObjectType):
    class Meta:
        model = assessment


class Query(graphene.ObjectType):
    all_assessments = graphene.List(AssessmentType)

    def resolve_all_assessments(self, info, **kwargs):
        return assessment.objects.all()


class CreateAssessment(graphene.Mutation):
    assessment = graphene.Field(AssessmentType)

    class Arguments:
        assigned_users_id = graphene.Int(required=True)
        enquiry_id = graphene.Int(required=True)
        student_country = graphene.String(required=True)
        university_id = graphene.Int(required=True)
        level_applying_for_id = graphene.Int(required=True)
        course_interested_id = graphene.Int(required=True)
        intake_interested_month_id = graphene.Int(required=True)
        intake_interested_year_id = graphene.Int(required=True)
        specialisation = graphene.String(required=True)
        duration = graphene.String(required=True)
        application_fee = graphene.String(required=True)
        tuition_fee = graphene.String(required=True)
        fee_currency = graphene.String(required=True)
        course_link = graphene.String(required=True)
        notes = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        assessment_instance = assessment.objects.create(
            assigned_users_id=kwargs.get('assigned_users_id'),
            enquiry_id=kwargs.get('enquiry_id'),
            student_country=kwargs.get('student_country'),
            university_id=kwargs.get('university_id'),
            level_applying_for_id=kwargs.get('level_applying_for_id'),
            course_interested_id=kwargs.get('course_interested_id'),
            intake_interested_month_id=kwargs.get('intake_interested_month_id'),
            intake_interested_year_id=kwargs.get('intake_interested_year_id'),
            specialisation=kwargs.get('specialisation'),
            duration=kwargs.get('duration'),
            application_fee=kwargs.get('application_fee'),
            tuition_fee=kwargs.get('tuition_fee'),
            fee_currency=kwargs.get('fee_currency'),
            course_link=kwargs.get('course_link'),
            notes=kwargs.get('notes')
        )
        return CreateAssessment(assessment=assessment_instance)


class Mutation(graphene.ObjectType):
    create_assessment = CreateAssessment.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
