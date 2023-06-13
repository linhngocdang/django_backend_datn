from django.contrib import admin
from .models import Employee, Doctor

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name','age','gender', 'email', 'contact', 'address','birthday','featured_img','classified']
admin.site.register(Employee, EmployeeAdmin)
# Register your models here.

class  DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'password']
admin.site.register( Doctor,  DoctorAdmin)
