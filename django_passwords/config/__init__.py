"""
This file ensures that the config folder is treated as a module.
It also sets the default settings module if it's not already set.
"""

import os

# Default to development settings if no settings module is specified
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.development')
