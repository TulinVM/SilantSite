# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Справочники для моделей техники, двигателей, трансмиссий и др.
class ModelReference(models.Model):
    CATEGORY_CHOICES = (
        ('engine', 'Модель двигателя'),
        ('transmission', 'Модель трансмиссии'),
        ('drive_axle', 'Модель ведущего моста'),
        ('steering_axle', 'Модель управляемого моста'),
        ('equipment', 'Модель техники'),
    )

    name = models.CharField(max_length=100, verbose_name="Наименование")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория модели")

    class Meta:
        verbose_name = "Справочник модели"
        verbose_name_plural = "Справочники моделей"

    def __str__(self):
        return f"{self.get_category_display()}: {self.name}"


# Справочники пользователей и Сервисных компаний техники .
class CustomUser(models.Model):
    CATEGORY_CHOICES = (
        ('client', 'Клиент'),
    )

    name = models.CharField(max_length=100, verbose_name="Наименование")
    groups = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Группы пользователей")

    class Meta:
        verbose_name = "Справочник пользователей"
        verbose_name_plural = "Справочники пользователей"

    def __str__(self):
        return f"{self.get_groups_display()}: {self.name}"


class ServiceName(models.Model):
    CATEGORY_CHOICES = (
        ('service_company', 'Сервисная компания'),
    )

    name = models.CharField(max_length=100, verbose_name="Наименование Сервисных компаний")
    groups = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Группа Сервисных компаний")

    class Meta:
        verbose_name = "Справочник Сервисных компаний"
        verbose_name_plural = "Справочник Сервисных компаний"

    def __str__(self):
        return f"{self.get_groups_display()}: {self.name}"

# Справочники комплектации техники .
class ModelEngine(models.Model):
    CATEGORY_CHOICES = (
        ('engine', 'Модель двигателя'),
    )

    name = models.CharField(max_length=100, verbose_name="Наименование")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория модели")

    class Meta:
        verbose_name = "Справочник модели"
        verbose_name_plural = "Справочники моделей"

    def __str__(self):
        return f"{self.get_category_display()}: {self.name}"
    

class ModelTransmission(models.Model):
    CATEGORY_CHOICES = (
        ('transmission', 'Модель трансмиссии'),
    )

    name = models.CharField(max_length=100, verbose_name="Наименование")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория модели")

    class Meta:
        verbose_name = "Справочник модели"
        verbose_name_plural = "Справочники моделей"

    def __str__(self):
        return f"{self.get_category_display()}: {self.name}"
    

class ModelDrive_axle(models.Model):
    CATEGORY_CHOICES = (
        ('drive_axle', 'Модель ведущего моста'),

    )
    name = models.CharField(max_length=100, verbose_name="Наименование")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория модели")

    class Meta:
        verbose_name = "Справочник модели"
        verbose_name_plural = "Справочники моделей"

    def __str__(self):
        return f"{self.get_category_display()}: {self.name}"


class ModelSteering_axle(models.Model):
    CATEGORY_CHOICES = (
        ('steering_axle', 'Модель управляемого моста'),

    )
    name = models.CharField(max_length=100, verbose_name="Наименование")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория модели")

    class Meta:
        verbose_name = "Справочник модели"
        verbose_name_plural = "Справочники моделей"

    def __str__(self):
        return f"{self.get_category_display()}: {self.name}"

       
class ModelEquipment(models.Model):
    CATEGORY_CHOICES = (
        ('equipment', 'Модель техники'),
    )
    name = models.CharField(max_length=100, verbose_name="Наименование")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория модели")

    class Meta:
        verbose_name = "Справочник модели"
        verbose_name_plural = "Справочники моделей"

    def __str__(self):
        return f"{self.get_category_display()}: {self.name}"
        
        


# Модель Машина
class Machine(models.Model):
    serial_number = models.CharField(max_length=100, unique=True, verbose_name='Зав. № машины')
    equipment = models.ForeignKey(
        ModelEquipment, on_delete=models.CASCADE, null=True, verbose_name='Модель техники'
    )
    engine_model = models.ForeignKey(
        ModelEngine, on_delete=models.CASCADE, null=True, verbose_name='Модель двигателя'
    )
    transmission_model = models.ForeignKey(
        ModelTransmission, on_delete=models.CASCADE, null=True, verbose_name='Модель трансмиссии'
    )
    drive_axle_model = models.ForeignKey(
        ModelDrive_axle, on_delete=models.CASCADE, null=True, verbose_name='Модель ведущего моста'
    )
    steerable_axle_model = models.ForeignKey(
        ModelSteering_axle, on_delete=models.CASCADE, null=True, verbose_name='Модель управляемого моста'
    )
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, verbose_name='Клиент'
    )
    service_company = models.ForeignKey(
        ServiceName, on_delete=models.CASCADE, null=True, verbose_name='Сервисная компания'
    )
    # другие поля модели...
    equipment_model = models.CharField(max_length=100, verbose_name='Модель оборудования') 
    engine_serial = models.CharField(max_length=100, verbose_name='Зав. № двигателя')  # Зав. № двигателя
    transmission_serial = models.CharField(max_length=100, verbose_name='Зав. № трансмиссии')  # Зав. № трансмиссии
    drive_axle_serial = models.CharField(max_length=100, verbose_name=' Зав. № ведущего моста')  # Зав. № ведущего моста
    steerable_axle_serial = models.CharField(max_length=100, verbose_name='Зав. № управляемого моста')  # Зав. № управляемого моста
    delivery_contract = models.CharField(max_length=255, verbose_name='Договор поставки №, дата')  # Договор поставки №, дата
    shipment_date = models.DateField(verbose_name='Дата отгрузки с завода')  # Дата отгрузки с завода
    receiver = models.CharField(max_length=255, verbose_name='Грузополучатель (конечный потребитель)')  # Грузополучатель (конечный потребитель)
    delivery_address = models.CharField(max_length=255, verbose_name='Адрес поставки (эксплуатации)')  # Адрес поставки (эксплуатации)
    delivery_date = models.DateField(verbose_name='Дата доставки')
    configuration = models.TextField(verbose_name='Комплектация (доп. опции)')  # Комплектация (доп. опции)


    def __str__(self):
        return self.serial_number
