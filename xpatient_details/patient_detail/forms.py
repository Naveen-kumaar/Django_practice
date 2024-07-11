from django import forms
from patient_detail.models import Patient
from patient_detail.models import Login
# Create your models here.
class Patientform(forms.ModelForm):
    class Meta:   #inner class , not a child class
        model = Patient
        fields ='__all__'

class Loginform(forms.ModelForm):
    class meta:
        model = Login
        fields ='__all__'