import os  # Standard library for interacting with the operating system

from dotenv import \
    load_dotenv  # Library to load environment variables from a .env file

# 🔹 Load environment variables from the .env file into the system environment
# This ensures that values like SECRET_KEY, DATABASE settings, and DJANGO_ENV are available.
load_dotenv()

# 🔹 Dynamically set the Django settings module based on the environment
# `os.getenv('DJANGO_ENV', 'development')`:
#    - Reads the DJANGO_ENV variable from the .env file.
#    - If DJANGO_ENV is not set, it defaults to 'development'.
# `f"config.{...}"` dynamically builds the settings module path:
#    - If DJANGO_ENV=development, it sets "config.development".
#    - If DJANGO_ENV=production, it sets "config.production".
# `os.environ.setdefault(...)` ensures the variable is only set **if it hasn't been set already**.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"config.{os.getenv('DJANGO_ENV', 'development')}"
)

# 🔹 Import Django's WSGI application handler
# WSGI (Web Server Gateway Interface) is the standard interface between web servers and Django applications.
from django.core.wsgi import get_wsgi_application

# 🔹 Initialize the WSGI application
# This tells Django to start the application using the correct settings module.
application = get_wsgi_application()
