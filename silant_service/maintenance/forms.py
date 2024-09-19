from django import forms
from .models import Maintenance




class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance  # Используем модель Machine
        fields = ['maintenance_type', 'maintenance_date', 'operating_hours', 'order_number',
                   'order_date', 'maintenance_organization', 'machine', 'service_company',]  # Укажите поля, которые хотите использовать в форме

        widgets = {
            'maintenance_date': forms.DateInput(attrs={'type': 'date'}), # Используем HTML5 input с type="date"
            'order_date': forms.DateInput(attrs={'type': 'date'}), # Используем HTML5 input с type="date"
        }

        class Meta:
            model = Maintenance
            fields = '__all__'


