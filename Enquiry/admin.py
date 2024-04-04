from django.contrib import admin
from django.db import models

from .models import enquiry, enquiry_status
from import_export.admin import ImportExportMixin
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage

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

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #
    #     admin_subject = "Enquiry Message"
    #     admin_message = (
    #         f"A new enquiry has been submitted:\n"
    #         f"Name: {obj.student_First_Name} {obj.student_Last_Name}\n"
    #         f"Email: {obj.student_email}\n"
    #         f"Passport: {obj.student_passport}\n"
    #         f"Source Enquiry: {obj.Source_Enquiry}\n"
    #         f"Phone: {obj.student_phone}\n"
    #         f"Alternate Phone: {obj.alternate_phone}\n"
    #         f"Address: {obj.student_address}\n"
    #         f"Country: {obj.student_country}\n"
    #         f"State: {obj.student_state}\n"
    #         f"City: {obj.student_city}\n"
    #         f"ZIP: {obj.student_zip}\n"
    #         f"Education: {obj.current_education}\n"
    #         f"Country Interested: {obj.country_interested}\n"
    #         f"University Interested: {obj.university_interested}\n"
    #         f"Course Interested: {obj.course_interested}\n"
    #         f"Level Applying For: {obj.level_applying_for}\n"
    #         f"Intake Interested: {obj.intake_interested}\n"
    #         f"Services Interested: {', '.join([str(service) for service in obj.Interested_Services.all()])}\n"
    #         f"Assigned Users: {obj.assigned_users}\n"
    #         f"Enquiry Status: {obj.enquiry_status}\n"
    #         f"Notes: {obj.notes}\n"
    #         f"\nView the details in the admin panel."
    #     )
    #     admin_email = settings.ADMIN_EMAIL
    #     admin_email_message = EmailMessage(admin_subject, admin_message, settings.DEFAULT_FROM_EMAIL, [admin_email])
    #     admin_email_message.send()
    #
    #     student_subject = "Thank You for Your Enquiry"
    #     student_message = (
    #         f"Thank you for your enquiry. We will get back to you shortly.\n"
    #         f"\nYour enquiry details:\n"
    #         f"Name: {obj.student_First_Name} {obj.student_Last_Name}\n"
    #         f"Email: {obj.student_email}\n"
    #         f"Passport: {obj.student_passport}\n"
    #         f"Source Enquiry: {obj.Source_Enquiry}\n"
    #         f"Phone: {obj.student_phone}\n"
    #         f"Alternate Phone: {obj.alternate_phone}\n"
    #         f"Address: {obj.student_address}\n"
    #         f"Country: {obj.student_country}\n"
    #         f"State: {obj.student_state}\n"
    #         f"City: {obj.student_city}\n"
    #         f"ZIP: {obj.student_zip}\n"
    #         f"Education: {obj.current_education}\n"
    #         f"Country Interested: {obj.country_interested}\n"
    #         f"University Interested: {obj.university_interested}\n"
    #         f"Course Interested: {obj.course_interested}\n"
    #         f"Level Applying For: {obj.level_applying_for}\n"
    #         f"Intake Interested: {obj.intake_interested}\n"
    #         f"Services Interested: {', '.join([str(service) for service in obj.Interested_Services.all()])}\n"
    #         f"Assigned Users: {obj.assigned_users}\n"
    #         f"Enquiry Status: {obj.enquiry_status}\n"
    #         f"Notes: {obj.notes}\n"
    #     )
    #     student_email = obj.student_email
    #     student_email_message = EmailMessage(student_subject, student_message, settings.DEFAULT_FROM_EMAIL, [student_email])
    #     student_email_message.send()
    #
    # def save_email(self, request, obj):
    #     super().save_email(self, request, obj)

        
admin.site.register(enquiry, EnquiryList)
# from django.contrib import admin
# from admin_charts.models import Chart

# # Register your models here.
# admin.site.register(Chart)
