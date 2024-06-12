from django.contrib import admin
from dbapp.models import students

# Register your models here.

class studentadmin(admin.ModelAdmin):
    stud_details =['studNO','studName','studfee','studAddress']

admin.site.register(students,studentadmin)
