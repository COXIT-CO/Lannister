from django.apps import AppConfig


class LannisterAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "lannister_app"

    def ready(self):
        import lannister_app.signals  # noqa
