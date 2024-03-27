from django.contrib import admin
from django.db import models

from .models import enquiry, enquiry_status
from import_export.admin import ImportExportMixin



# Register your models here.





class EnquiryList(ImportExportMixin,admin.ModelAdmin):
    fieldsets = (
        ("Student Info", {"fields": ("student_First_Name", "student_Last_Name", "student_passport",'Source_Enquiry')}),
        ("Contact Info", {"fields": (
            "student_phone", "alternate_phone", "student_email", "student_address", "student_country", "student_state",
            "student_city", "student_zip")}),
        ("Education Info", {"fields": ("current_education",)}),
        ("Enquiry Info", {"fields": (
            "country_interested", "university_interested","level_applying_for", "course_interested",
            "intake_interested", "Interested_Services")}),
        ("For Counsellor", {"fields": ("assigned_users", "enquiry_status", "notes")}),
    )
    jazzmin_section_order = ("Student Info", "Contact Info", "Education Info", "Enquiry Info", "For Counsellor")

    actions = ['update_enquiry_status']
    list_display = (
        'student_First_Name', 'student_Last_Name', 'student_phone', 'student_email', 'country_interested',
        'university_interested','Interested_service',
        'course_interested', 'level_applying_for', 'intake_interested',
        'assigned_users', 'enquiry_status','notes', 'total_price','Source_Enquiry')


    list_filter = (
        'student_First_Name', 'student_phone', 'student_email', 'current_education',
        'university_interested', 'course_interested', 'assigned_users', 'enquiry_status','Source_Enquiry')

    list_display_links = ('student_First_Name',)
    list_per_page = 10

    search_fields = ('student_First_Name', 'student_Last_Name', 'student_phone', 'student_email', 'current_education',
                     'country_interested',
                     'university_interested',
                     'course_interested', 'level_applying_for', 'intake_interested',
                     'assigned_users', 'enquiry_status',)



#Update enquiry status to Processed is a Action Function to Update the status of all the selected enquiry to Processed
    def update_enquiry_status(modeladmin, request, queryset):
        processed_status = enquiry_status.objects.get(status='Processed')
        queryset.update(enquiry_status=processed_status)
    update_enquiry_status.short_description = "Update status to Processed"


#Interested_service is a function to get the services selected by the student AND SHOW IT IN LIST DISPLAY
    def Interested_service(self, obj):
        return ', '.join([a.Services for a in obj.Interested_Services.all()])


#Total Price is a function to get the total price of the services selected by the student AND SHOW IT IN LIST DISPLAY

    def total_price(self, obj):
        return obj.Interested_Services.aggregate(total=models.Sum('Price'))['total'] or 0

    total_price.short_description = "Total Price"


admin.site.register(enquiry, EnquiryList)



