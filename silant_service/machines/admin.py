from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Machine
from maintenance.models import Maintenance
from complaints.models import Complaint
# from django import forms

admin.site.register(Machine)
admin.site.register(Maintenance)
admin.site.register(Complaint)

# from django.contrib import admin
# # from .models import Machine
# from .forms import MachineForm  # Импортируем форму

# class MachineAdmin(admin.ModelAdmin):
#     form = MachineForm  # Указываем кастомную форму

# admin.site.register(MachineAdmin)
