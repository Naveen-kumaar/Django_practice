from django.contrib import admin
from patient_detail.models import Patient

# Register your models here.
class Patient_admin(admin.ModelAdmin):
    patient_details= ['patient_name','patient_age','patient_address','patient_contactNo','patient_injury']

admin.site.register(Patient,Patient_admin)