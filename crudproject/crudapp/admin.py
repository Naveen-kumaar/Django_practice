from django.contrib import admin
from crudapp.models import student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list = ['sno','sname','sname','saddress']

admin.site.register(student,StudentAdmin)
