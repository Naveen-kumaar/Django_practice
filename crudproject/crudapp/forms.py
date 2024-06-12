from django import forms
from crudapp.models import student
# Create your models here.
class studentform(forms.ModelForm):
    class Meta:   #inner class , not a child class
        model = student
        fields ='__all__'
