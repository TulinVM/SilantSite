from django.apps import AppConfig


class MachinesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'machines'

    def ready(self):
        # Импортируем signals для подключения сигналов
        import machines.signals