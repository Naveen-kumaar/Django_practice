from django import forms
from patient_detail.models import Patient
# Create your models here.
class Patientform(forms.ModelForm):
    class Meta:   #inner class , not a child class
        model = Patient
        fields ='__all__'