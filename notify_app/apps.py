from django.apps import AppConfig


class NotifyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notify_app'

    # Activate the signal to run
    def ready(self):
        import notify_app.signals
