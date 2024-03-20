from django.contrib import admin
from .models import Detail_Enquiry  # Make sure to import your model correctly


class DetailEnquiryAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('Current_Enquiry', 'level', 'Father_Occupation', 'Father_Annual_Income')

    # Enable search
    search_fields = ('Current_Enquiry__student_First_Name', 'Father_Occupation')

    # Enable filters
    list_filter = (
    'level', 'Work_Experience', 'Toefl_Exam', 'ielts_Exam', 'PTE_Exam', 'Duolingo_Exam', 'Gre_Exam', 'Gmat_Exam',
    'Refusal')

    # Fieldsets to organize the form view
    fieldsets = (
        ('Basic Information', {
            'fields': ('Current_Enquiry', 'level', 'Work_Experience')
        }),
        ('Examination Details', {
            'fields': ('Toefl_Exam', 'ielts_Exam', 'PTE_Exam', 'Duolingo_Exam', 'Gre_Exam', 'Gmat_Exam'),
        }),
        ('Family Details', {
            'fields': ('Father_Occupation', 'Father_Annual_Income'),
        }),
        ('Document Uploads', {
            'fields': (
            'Twelveth_Document', 'Tenth_Document', 'Graduation_Marksheet', 'Graduation_Certificate', 'UG_Marksheet',
            'UG_Certificate', 'Work_Experience_Document', 'Passport_Document', 'Offer_Letter', 'Ielts_Result',
            'Toefl_Result', 'PTE_Result', 'Duolingo_Result', 'Gre_Result', 'Gmat_Result'),
        }),
    )

    # Optionally, customize the form to use select2 widgets for foreign keys
    # This can make the interface more user-friendly for models with many foreign keys.
    # You would need to override the formfield_for_foreignkey method or use a third-party package like django-autocomplete-light.


admin.site.register(Detail_Enquiry, DetailEnquiryAdmin)
