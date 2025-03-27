from django.apps import AppConfig


class SecureAppConfig(AppConfig):
    """
    Configuration class for the SecureApp Django application.
    This class ensures that signals are imported when the app is ready.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "secureapp"

    def ready(self):
        """Ensures signals are imported after app initialization."""
        import secureapp.signals  # ✅ Ensure signals are loaded correctly
