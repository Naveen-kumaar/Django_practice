from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=30)
    patient_age = models.IntegerField()
    patient_address = models.CharField(max_length=50)
    patient_contactNo = models.IntegerField()
    patient_injury = models.CharField(max_length=40)

