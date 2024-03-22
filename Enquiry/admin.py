from django.contrib import admin
from .models import enquiry


# Register your models here.
class EnquiryList(admin.ModelAdmin):
    fieldsets = (
        ("Student Info", {"fields": ("student_First_Name", "student_Last_Name", "student_passport")}),
        ("Contact Info", {"fields": (
            "student_phone", "alternate_phone", "student_email", "student_address", "student_country", "student_state",
            "student_city", "student_zip")}),
        ("Education Info", {"fields": ("current_education",)}),
        ("Enquiry Info", {"fields": (
            "country_interested", "university_interested", "course_interested", "level_applying_for",
            "intake_interested")}),
        ("For Counsellor", {"fields": ("assigned_users", "enquiry_status", "notes")}),
    )
    jazzmin_section_order = ("Student Info", "Contact Info", "Education Info", "Enquiry Info", "For Counsellor")

    list_display = (
        'student_First_Name', 'student_Last_Name', 'student_phone', 'student_email', 'country_interested',
        'university_interested',
        'course_interested', 'level_applying_for', 'intake_interested',
        'assigned_users', 'enquiry_status','notes', )

    list_filter = (
        'student_First_Name', 'student_phone', 'student_email', 'current_education',
        'university_interested', 'course_interested', 'assigned_users', 'enquiry_status',)

    list_display_links = ('student_First_Name',)
    list_per_page = 10

    search_fields = ('student_First_Name', 'student_Last_Name', 'student_phone', 'student_email', 'current_education',
                     'country_interested',
                     'university_interested',
                     'course_interested', 'level_applying_for', 'intake_interested',
                     'assigned_users', 'enquiry_status',)


admin.site.register(enquiry, EnquiryList)
