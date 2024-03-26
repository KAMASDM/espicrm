import graphene
from graphene_django.types import DjangoObjectType
from .models import enquiry


class EnquiryType(DjangoObjectType):
    class Meta:
        model = enquiry


class Query(graphene.ObjectType):
    all_enquiries = graphene.List(EnquiryType)

    def resolve_all_enquiries(self, info, **kwargs):
        return enquiry.objects.all()


class CreateEnquiry(graphene.Mutation):
    enquiry = graphene.Field(EnquiryType)

    class Arguments:
        student_first_name = graphene.String(required=True)
        student_last_name = graphene.String(required=True)
        student_passport = graphene.String(required=True)
        student_phone = graphene.String(required=True)
        alternate_phone = graphene.String()
        student_email = graphene.String(required=True)
        student_address = graphene.String(required=True)
        student_country = graphene.String(required=True)
        student_state = graphene.String(required=True)
        student_city = graphene.String(required=True)
        student_zip = graphene.String(required=True)
        current_education_id = graphene.Int(required=True)
        country_interested = graphene.String(required=True)
        university_interested_id = graphene.Int(required=True)
        course_interested_id = graphene.Int(required=True)
        level_applying_for_id = graphene.Int(required=True)
        intake_interested_month = graphene.String(required=True)
        intake_interested_year_id = graphene.Int(required=True)
        assigned_users_id = graphene.Int(required=True)
        enquiry_status_id = graphene.Int(required=True)
        notes = graphene.String()

    def mutate(self, info, **kwargs):
        enquiry_instance = enquiry.objects.create(
            student_First_Name=kwargs.get('student_first_name'),
            student_Last_Name=kwargs.get('student_last_name'),
            student_passport=kwargs.get('student_passport'),
            student_phone=kwargs.get('student_phone'),
            alternate_phone=kwargs.get('alternate_phone'),
            student_email=kwargs.get('student_email'),
            student_address=kwargs.get('student_address'),
            student_country=kwargs.get('student_country'),
            student_state=kwargs.get('student_state'),
            student_city=kwargs.get('student_city'),
            student_zip=kwargs.get('student_zip'),
            current_education_id=kwargs.get('current_education_id'),
            country_interested=kwargs.get('country_interested'),
            university_interested_id=kwargs.get('university_interested_id'),
            course_interested_id=kwargs.get('course_interested_id'),
            level_applying_for_id=kwargs.get('level_applying_for_id'),
            intake_interested_month=kwargs.get('intake_interested_month'),
            intake_interested_year_id=kwargs.get('intake_interested_year_id'),
            assigned_users_id=kwargs.get('assigned_users_id'),
            enquiry_status_id=kwargs.get('enquiry_status_id'),
            notes=kwargs.get('notes')
        )
        return CreateEnquiry(enquiry=enquiry_instance)


class Mutation(graphene.ObjectType):
    create_enquiry = CreateEnquiry.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
