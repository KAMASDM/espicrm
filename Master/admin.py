from django.contrib import admin

# Register your models here.
from .models import country, course_levels, intake, current_education, documents_required, course_requirements, \
    enquiry_status, application_status, Course, university, intake_Year, assessment_status, Edu_Level,Work_Experience, \
    ielts_Exam, PTE_Exam, Toefl_Exam, Duolingo_Exam, Gre_Exam, Gmat_Exam, Rejection_Reason


from import_export.admin import ImportExportMixin



# Register your models here.


class CourseListAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('university', 'course_name', 'course_levels', 'intake', 'documents_required', 'course_requirements', 'Active')

    list_filter = ('university', 'course_name', 'course_levels', 'intake', 'documents_required', 'course_requirements', 'Active')

    list_display_links = None
    list_per_page = 20



class UniversityListAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'univ_name', 'country', 'univ_desc', 'univ_logo', 'univ_phone', 'univ_email',
        'univ_website', 'assigned_users')

    list_filter = ('univ_name', 'country', 'univ_phone', 'univ_email', 'assigned_users')

    list_display_links = ('univ_name'),
    list_per_page = 10







admin.site.register(country)
admin.site.register(course_levels)
admin.site.register(intake)
admin.site.register(intake_Year)
admin.site.register(current_education)
admin.site.register(documents_required)
admin.site.register(course_requirements)
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




# Register your models here.
