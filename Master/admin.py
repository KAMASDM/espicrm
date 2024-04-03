from django.contrib import admin

# Register your models here.
from .models import country, course_levels, intake, current_education, documents_required, \
    enquiry_status, application_status, Course, university, assessment_status, Edu_Level,Work_Experience, \
     Rejection_Reason
from Master.models import twelfth_std_percentage_requirement, bachelor_requirement, masters_requirement, tenth_std_percentage_requirement, \
    ielts_Exam, PTE_Exam, Toefl_Exam, Duolingo_Exam, Gre_Exam, Gmat_Exam,Available_Services,Detail_Enquiry_Status,Enquiry_Source,Payment_Type, \
    Payment_Status, Payment_Mode, CountryInterested


from import_export.admin import ImportExportMixin



# Register your models here.


class CourseListAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id','university', 'course_name', 'course_levels','display_intakes','tenth_std_percentage_requirement','twelfth_std_percentage_requirement','bachelor_requirement','masters_requirement',
                          'Toefl_Exam','ielts_Exam','PTE_Exam','Duolingo_Exam','Gre_Exam', 'Gmat_Exam','Remark','Active')

    list_filter = ('university', 'course_name', 'course_levels', 'intake', 'documents_required','tenth_std_percentage_requirement','twelfth_std_percentage_requirement','bachelor_requirement','masters_requirement',
                          'Toefl_Exam','ielts_Exam','PTE_Exam','Duolingo_Exam','Gre_Exam', 'Gmat_Exam','Active')

    fieldsets = ( ('Course Details', {
                   'fields': ('university', 'course_name', 'course_levels', 'intake', 'documents_required', 'Active')
                }),
                ('Course Requirements', {
                    'fields': ('tenth_std_percentage_requirement','twelfth_std_percentage_requirement','bachelor_requirement','masters_requirement',
                          'Toefl_Exam','ielts_Exam','PTE_Exam','Duolingo_Exam','Gre_Exam', 'Gmat_Exam',
                            )
                }),
                ('Notes', {
                    'fields': ('Remark',)
                }),

    )

    list_display_links = ('id','university',)
    list_per_page = 20

    def display_intakes(self, obj):
        """
        Returns a comma-separated list of intake months and years from the ManyToManyField.
        """
        # Concatenates intake_month and intake_year for each intake, separated by a space, and then joins all into a comma-separated list
        return ", ".join([f"{intake.intake_Name} {intake.intake_month} {intake.intake_year}" for intake in obj.intake.all()])
    display_intakes.short_description = 'Intakes'  # Sets the column name in the admin list view






class UniversityListAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'univ_name', 'country', 'univ_desc',
        'univ_website','application_form','ielts_Exam','PTE_Exam','Toefl_Exam','Duolingo_Exam','Gre_Exam', 'Gmat_Exam','Remark','assigned_users')

    list_filter = ('univ_name', 'country', 'univ_phone', 'univ_email', 'assigned_users','ielts_Exam','PTE_Exam','Toefl_Exam','Duolingo_Exam','Gre_Exam', 'Gmat_Exam')
    fieldsets = (
        ('University Details', {
            'fields': ('univ_name', 'country', 'univ_desc', 'univ_logo',
                       'application_form' ,'newsletter','Active')
        }),
        ('Contact Information', {
            'fields': ('univ_phone', 'univ_email', 'univ_website', 'assigned_users')
        }),
        ('Requirements & Status', {
            'fields': ('tenth_std_percentage_requirement','twelfth_std_percentage_requirement','bachelor_requirement','masters_requirement',
                       'Toefl_Exam','ielts_Exam','PTE_Exam','Duolingo_Exam','Gre_Exam', 'Gmat_Exam',
                       )
        }),
         ('Notes', {
            'fields': ('Remark',)
        }),


    )

    list_display_links = ('univ_name'),
    list_per_page = 10







admin.site.register(country)
admin.site.register(course_levels)
admin.site.register(intake)
admin.site.register(current_education)
admin.site.register(documents_required)
admin.site.register(enquiry_status)
admin.site.register(application_status)
admin.site.register(Course, CourseListAdmin)
admin.site.register(university, UniversityListAdmin)
admin.site.register(assessment_status)
admin.site.register(Edu_Level)
admin.site.register(Work_Experience)
admin.site.register(ielts_Exam)
admin.site.register(PTE_Exam)
admin.site.register(Toefl_Exam)
admin.site.register(Duolingo_Exam)
admin.site.register(Gre_Exam)
admin.site.register(Gmat_Exam)
admin.site.register(Rejection_Reason)
admin.site.register(tenth_std_percentage_requirement)
admin.site.register(twelfth_std_percentage_requirement)
admin.site.register(bachelor_requirement)
admin.site.register(masters_requirement)
admin.site.register(Available_Services)
admin.site.register(Detail_Enquiry_Status)
admin.site.register(Enquiry_Source)
admin.site.register(Payment_Type)
admin.site.register(Payment_Status)
admin.site.register(Payment_Mode)
admin.site.register(CountryInterested)






# Register your models here.
