# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from machines.models import Machine, ModelReference


# # Справочники для моделей техники, двигателей, трансмиссий и др.
# class ModelReference(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

    
# Модель ТО (Техническое обслуживание)
class Maintenance(models.Model):
    maintenance_type = models.ForeignKey(ModelReference, related_name='maintenance_types', on_delete=models.SET_NULL, null=True, verbose_name='Вид ТО')  # Вид ТО
    maintenance_date = models.DateField(verbose_name='Дата проведения ТО')  # Дата проведения ТО
    operating_hours = models.PositiveIntegerField(verbose_name='Наработка, м/час')  # Наработка, м/час
    order_number = models.CharField(max_length=100, verbose_name='№ заказ-наряда')  # № заказ-наряда
    order_date = models.DateField(verbose_name='Дата заказ-наряда')  # Дата заказ-наряда
    maintenance_organization = models.ForeignKey(ModelReference, related_name='maintenance_organizations', on_delete=models.SET_NULL, null=True, verbose_name='Организация, проводившая ТО')  # Организация, проводившая ТО
    machine = models.ForeignKey(Machine, related_name='maintenances', on_delete=models.CASCADE, verbose_name='Машина')  # Машина
    service_company = models.ForeignKey(User, related_name='service_company_maintenances', on_delete=models.SET_NULL, null=True, limit_choices_to={'groups__name': 'Service'}, verbose_name='Сервисная компания')  # Сервисная компания

    def __str__(self):
        return f"ТО {self.maintenance_type} для машины {self.machine.serial_number}"
