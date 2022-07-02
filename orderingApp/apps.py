from django.apps import AppConfig


class OrderingappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orderingApp'

    def ready(self):
        import orderingApp.signals
