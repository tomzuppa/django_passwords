"""
Initialize configuration settings module based on the environment.

This file ensures that:
- The 'config' directory is recognized as a Python module.
- The Django settings module is set dynamically, depending on the
  environment (development or production).

Environment Variable:
- DJANGO_ENV: Determines the execution environment. Possible values:
  - 'development' (default)
  - 'production'

  TO SWITCH TO PRODUCTION (FROM TERMINAL):
    export DJANGO_ENV=production
"""

import os

# Retrieve the current environment from DJANGO_ENV; defaults to 'development' if not set.
DJANGO_ENV = os.getenv("DJANGO_ENV", "development")

# Determine the appropriate Django settings module based on DJANGO_ENV.
if DJANGO_ENV == "production":
    settings_module = "config.production"
else:
    settings_module = "config.development"

# Set the DJANGO_SETTINGS_MODULE environment variable.
# This tells Django explicitly which settings module to use.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
