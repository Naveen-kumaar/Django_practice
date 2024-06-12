from django.db import models

# Create your models here.
class students(models.Model):
    studNO = models.IntegerField()
    studName = models.CharField(max_length=30)
    studfee = models.IntegerField()
    studAddress = models.CharField(max_length=30)
    #these are table attributes,database table la enna enna table venumo atha solrathu
    #python manage.py makemigrate /mothalla ready  panni vaikirom
    #db ku python ku nadakura conversation make db ready
    #python manage.py migrate /kudukum pothu than namakana table create athu
def __str__(self):
    return 'students details are shared'

