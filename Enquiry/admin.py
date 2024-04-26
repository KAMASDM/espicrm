
from typing import Any

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportMixin

from .models import enquiry, enquiry_status

# Register your models here.


# class BranchListFilter(admin.SimpleListFilter):
#     title = _('Branch wise Filter')
#     parameter_name = "branch"
    
#     def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
#         customUser = get_user_model()
#         branch = Group.objects.get(name='Branch')
#         branch_name = customUser.objects.filter(groups = branch)
        
#         __branch_list = list(branch_name.values_list('username',flat=True))
#         branch_list = [ (i,i) for i in __branch_list]
#         return branch_list
    
#     def queryset(self, request: Any, queryset: models.QuerySet[Any]) -> models.QuerySet[Any] | None:
#         if self.value():
#             branch= get_user_model().objects.get(username=self.value())
#             return enquiry.objects.filter(
#                 Q(created_by__created_by=branch)|
#                 Q(created_by=branch))




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
        ("For Counsellor", {"fields": ("assigned_users","enquiry_status","EnquiryFollowup","notes")}),
    )
    jazzmin_section_order = ("Student Info", "Contact Info", "Education Info", "Enquiry Info", "For Counsellor")

    actions = ['update_enquiry_status']
    list_display = (
        'student_First_Name', 'student_Last_Name', 'student_phone', 'student_email', 'country_interested',
        'university_interested','Interested_service',
        'course_interested', 'level_applying_for', 'intake_interested',
        'assigned_users', 'enquiry_status','notes', 'total_price','Source_Enquiry','created_by')


    list_filter = (
        'student_First_Name', 'student_phone', 'student_email', 'current_education',
        'university_interested', 'course_interested', 'assigned_users', 'enquiry_status','Source_Enquiry',
        'created_by')

    list_display_links = ('student_First_Name',)
    list_per_page = 10

    search_fields = ('student_First_Name', 'student_Last_Name', 'student_phone', 'student_email', 'current_education',
                     'country_interested',
                     'university_interested',
                     'course_interested', 'level_applying_for', 'intake_interested',
                     'assigned_users','enquiry_status','EnquiryFollowup')



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
    
    def save_model(self, request, obj, form, change) -> None:
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)
    
admin.site.register(enquiry, EnquiryList)

