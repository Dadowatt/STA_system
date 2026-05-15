from django.apps import AppConfig


class EntriesConfig(AppConfig):
    name = 'entries'

    def ready(self):
        default_auto_field = 'django.db.models.BigAutoField'
        import entries.signals


