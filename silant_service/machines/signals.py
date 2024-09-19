# machines/signals.py

from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_user_roles(sender, **kwargs):
    # Создаем или получаем группы
    guest_group, created = Group.objects.get_or_create(name='Гость')
    client_group, created = Group.objects.get_or_create(name='Клиент')
    service_group, created = Group.objects.get_or_create(name='Сервисная организация')
    manager_group, created = Group.objects.get_or_create(name='Менеджер')

    # Определяем разрешения для каждой группы
    guest_permissions = ['machine_list']
    client_permissions = ['machine_list', 'machine_detail']
    service_permissions = ['machine_list', 'machine_detail', 'machine_update', 'machine_create']
    manager_permissions = ['machine_list', 'machine_detail', 'machine_update', 'machine_create', 'machine_delete']

    # Применяем разрешения к группам
    for perm in guest_permissions:
        permission = Permission.objects.get(codename=perm)
        guest_group.permissions.add(permission)

    for perm in client_permissions:
        permission = Permission.objects.get(codename=perm)
        client_group.permissions.add(permission)

    for perm in service_permissions:
        permission = Permission.objects.get(codename=perm)
        service_group.permissions.add(permission)

    for perm in manager_permissions:
        permission = Permission.objects.get(codename=perm)
        manager_group.permissions.add(permission)
