from django import forms
from .models import Machine
from .signals import Group



class MachineForm(forms.ModelForm):
    model = Machine  # Используем модель Machine
    delivery_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        # input_formats=['%Y-%m-%d'],  # Указываем ожидаемый формат даты
        label='Дата доставки'
    )
    shipment_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        # input_formats=['%Y-%m-%d'],  # Указываем ожидаемый формат даты
        label='Дата отгрузки с завода'
    )

    class Meta:
        model = Machine  # Используем модель Machine
        fields = ['serial_number', 'equipment', 'equipment_model', 'engine_model', 
                  'engine_serial', 'transmission_model', 'transmission_serial', 
                  'drive_axle_model', 'drive_axle_serial', 'steerable_axle_model', 
                  'steerable_axle_serial', 'delivery_date', 'delivery_contract', 
                  'receiver', 'delivery_address', 'shipment_date', 'configuration', 
                  'client', 'service_company']  # Укажите поля, которые хотите использовать в форме

        # widgets = {
        #     'delivery_date': forms.DateInput(attrs={'type': 'date'}), # Используем HTML5 input с type="date"
        #     'shipment_date': forms.DateInput(attrs={'type': 'date'}), # Используем HTML5 input с type="date"
        # }

        class Meta:
            model = Machine
            fields = '__all__'


# from django.contrib.auth.models import User

# ROLE_CHOICES = (
#     ('guest', 'Гость'),
#     ('client', 'Клиент'),
#     ('service', 'Сервисная организация'),
#     ('manager', 'Менеджер'),
# )

# class UserRegistrationForm(forms.ModelForm):
#     role = forms.ChoiceField(choices=ROLE_CHOICES, label="Роль")

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'role']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         role = self.cleaned_data["role"]

#         if commit:
#             user.save()
#             assign_role_to_user(user, role)

#         return user

# def assign_role_to_user(user, role):
#     """
#     Назначает пользователя в соответствующую группу в зависимости от выбранной роли.
#     """
#     if role == 'guest':
#         group = Group.objects.get(name='Гость')
#     elif role == 'client':
#         group = Group.objects.get(name='Клиент')
#     elif role == 'service':
#         group = Group.objects.get(name='Сервисная организация')
#     elif role == 'manager':
#         group = Group.objects.get(name='Менеджер')
#     else:
#         return

#     user.groups.add(group)