from django import forms
from .models import Complaint, operating_hours




class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint  # Используем модель
        fields = ['failure_date', operating_hours, ]  # Укажите поля, которые хотите использовать в форме
        
        delivery_date = forms.DateField(
            widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        # input_formats=['%Y-%m-%d'],  # Указываем ожидаемый формат даты
        )
        shipment_date = forms.DateField(
            widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        # input_formats=['%Y-%m-%d'],  # Указываем ожидаемый формат даты
        )
        

        class Meta:
            model = Complaint
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