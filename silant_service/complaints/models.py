# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from machines.models import Machine, ModelReference



# Модель Рекламации
class Complaint(models.Model):
    failure_date = models.DateField(verbose_name='Дата отказа')  # Дата отказа
    operating_hours = models.PositiveIntegerField(verbose_name='Наработка, м/час')  # Наработка, м/час
    failure_node = models.ForeignKey(ModelReference, related_name='failure_nodes', on_delete=models.SET_NULL, null=True, verbose_name='Узел отказа')  # Узел отказа
    failure_description = models.TextField(verbose_name='Описание отказа')  # Описание отказа
    recovery_method = models.ForeignKey(ModelReference, related_name='recovery_methods', on_delete=models.SET_NULL, null=True, verbose_name='')  # Способ восстановления
    spare_parts_used = models.TextField(verbose_name='Используемые запасные части')  # Используемые запасные части
    recovery_date = models.DateField(verbose_name='Дата восстановления')  # Дата восстановления
    downtime = models.DurationField(verbose_name='Время простоя техники')  # Время простоя техники
    machine = models.ForeignKey(Machine, related_name='complaints', on_delete=models.CASCADE, verbose_name='Машина')  # Машина
    service_company = models.ForeignKey(User, related_name='service_company_complaints', on_delete=models.SET_NULL, null=True, limit_choices_to={'groups__name': 'Service'}, verbose_name='Сервисная компания')  # Сервисная компания

    def __str__(self):
        return f"Рекламация {self.machine.serial_number} от {self.failure_date}"
    
    def save(self, *args, **kwargs):
        # Автоматический расчет времени простоя техники
        if self.recovery_date and self.failure_date:
            self.downtime = self.recovery_date - self.failure_date
        super().save(*args, **kwargs)