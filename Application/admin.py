from django.contrib import admin
from .models import Application


# Register your models here.


class ApplicationList(admin.ModelAdmin):
    list_display = (
        'sop', 'passport', 'ielts', 'gre', 'gmat', 'toefl', 'pte',
        'application_status',)


admin.site.register(Application, ApplicationList)
