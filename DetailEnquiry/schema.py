import graphene
from graphene_django.types import DjangoObjectType
from .models import Detail_Enquiry


class DetailEnquiryType(DjangoObjectType):
    class Meta:
        model = Detail_Enquiry


class Query(graphene.ObjectType):
    all_detail_enquiries = graphene.List(DetailEnquiryType)

    def resolve_all_detail_enquiries(self, info, **kwargs):
        return Detail_Enquiry.objects.all()


class CreateDetailEnquiry(graphene.Mutation):
    detail_enquiry = graphene.Field(DetailEnquiryType)

    class Arguments:
        current_enquiry_id = graphene.Int(required=True)
        level_id = graphene.Int(required=True)
        work_experience_id = graphene.Int(required=True)
        toefl_exam_id = graphene.Int(required=True)
        ielts_exam_id = graphene.Int(required=True)
        pte_exam_id = graphene.Int(required=True)
        duolingo_exam_id = graphene.Int(required=True)
        gre_exam_id = graphene.Int(required=True)
        gmat_exam_id = graphene.Int(required=True)
        father_occupation = graphene.String(required=True)
        father_annual_income = graphene.Float(required=True)
        refusal_id = graphene.Int(required=True)
        twelveth_document = graphene.String(required=True)
        tenth_document = graphene.String(required=True)
        graduation_marksheet = graphene.String(required=True)
        graduation_certificate = graphene.String(required=True)
        ug_marksheet = graphene.String(required=True)
        ug_certificate = graphene.String(required=True)
        work_experience_document = graphene.String(required=True)
        passport_document = graphene.String(required=True)
        offer_letter = graphene.String(required=True)
        ielts_result = graphene.String(required=True)
        toefl_result = graphene.String(required=True)
        pte_result = graphene.String(required=True)
        duolingo_result = graphene.String(required=True)
        gre_result = graphene.String(required=True)
        gmat_result = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        detail_enquiry_instance = Detail_Enquiry.objects.create(
            Current_Enquiry_id=kwargs.get('current_enquiry_id'),
            level_id=kwargs.get('level_id'),
            Work_Experience_id=kwargs.get('work_experience_id'),
            Toefl_Exam_id=kwargs.get('toefl_exam_id'),
            ielts_Exam_id=kwargs.get('ielts_exam_id'),
            PTE_Exam_id=kwargs.get('pte_exam_id'),
            Duolingo_Exam_id=kwargs.get('duolingo_exam_id'),
            Gre_Exam_id=kwargs.get('gre_exam_id'),
            Gmat_Exam_id=kwargs.get('gmat_exam_id'),
            Father_Occupation=kwargs.get('father_occupation'),
            Father_Annual_Income=kwargs.get('father_annual_income'),
            Refusal_id=kwargs.get('refusal_id'),
            Twelveth_Document=kwargs.get('twelveth_document'),
            Tenth_Document=kwargs.get('tenth_document'),
            Graduation_Marksheet=kwargs.get('graduation_marksheet'),
            Graduation_Certificate=kwargs.get('graduation_certificate'),
            UG_Marksheet=kwargs.get('ug_marksheet'),
            UG_Certificate=kwargs.get('ug_certificate'),
            Work_Experience_Document=kwargs.get('work_experience_document'),
            Passport_Document=kwargs.get('passport_document'),
            Offer_Letter=kwargs.get('offer_letter'),
            Ielts_Result=kwargs.get('ielts_result'),
            Toefl_Result=kwargs.get('toefl_result'),
            PTE_Result=kwargs.get('pte_result'),
            Duolingo_Result=kwargs.get('duolingo_result'),
            Gre_Result=kwargs.get('gre_result'),
            Gmat_Result=kwargs.get('gmat_result')
        )
        return CreateDetailEnquiry(detail_enquiry=detail_enquiry_instance)


class Mutation(graphene.ObjectType):
    create_detail_enquiry = CreateDetailEnquiry.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
