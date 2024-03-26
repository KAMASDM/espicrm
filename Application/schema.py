import graphene
from graphene_django.types import DjangoObjectType
from .models import Application
from Assessment.schema import AssessmentType
from Master.schema import ApplicationStatusType
from Enquiry.schema import EnquiryType


class ApplicationType(DjangoObjectType):
    class Meta:
        model = Application


class Query(graphene.ObjectType):
    all_applications = graphene.List(ApplicationType)

    def resolve_all_applications(self, info, **kwargs):
        return Application.objects.all()


class CreateApplication(graphene.Mutation):
    application = graphene.Field(ApplicationType)

    class Arguments:
        assessment_id = graphene.Int(required=True)
        sop = graphene.String()
        cv = graphene.String()
        passport = graphene.String()
        ielts = graphene.String()
        gre = graphene.String()
        toefl = graphene.String()
        gmat = graphene.String()
        pte = graphene.String()
        work_experience = graphene.String()
        diploma_marksheet = graphene.String()
        bachelor_marksheet = graphene.String()
        master_marksheet = graphene.String()
        other_documents = graphene.String()
        application_status_id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        application_instance = Application.objects.create(
            application_id=kwargs.get('assessment_id'),
            sop=kwargs.get('sop'),
            cv=kwargs.get('cv'),
            passport=kwargs.get('passport'),
            ielts=kwargs.get('ielts'),
            gre=kwargs.get('gre'),
            toefl=kwargs.get('toefl'),
            gmat=kwargs.get('gmat'),
            pte=kwargs.get('pte'),
            work_experience=kwargs.get('work_experience'),
            diploma_marksheet=kwargs.get('diploma_marksheet'),
            bachelor_marksheet=kwargs.get('bachelor_marksheet'),
            master_marksheet=kwargs.get('master_marksheet'),
            other_documents=kwargs.get('other_documents'),
            application_status_id=kwargs.get('application_status_id')
        )
        return CreateApplication(application=application_instance)


class Mutation(graphene.ObjectType):
    create_application = CreateApplication.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
