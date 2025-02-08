from django.apps import AppConfig  # Import the base AppConfig class from Django

class SecureappConfig(AppConfig):  # Defines the configuration for the "secureapp" application
    """
    Configuration class for the SecureApp Django application.
    This class defines settings specific to the application.
    """

    default_auto_field = 'django.db.models.BigAutoField'  
    # Specifies the default type of primary key for models in this app (BigAutoField is optimized for large datasets)

    name = 'secureapp'  
    # Defines the application name as 'secureapp' (must match the folder name of the app)
