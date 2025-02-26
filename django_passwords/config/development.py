"""
Development settings for Django.
These settings are used when running the project in development mode.
"""

from .base import *  # Import all shared settings from base.py

# Enable debug mode (useful for debugging but should NEVER be enabled in production)
DEBUG = True

# Allow all hosts (for local development only)
ALLOWED_HOSTS = ['*']

# Database settings (Uses SQLite for local development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Uses SQLite (lightweight database)
        'NAME': BASE_DIR / 'database/db.sqlite3',
    }
}

# Security settings (Relaxed for local development)
CSRF_COOKIE_SECURE = False  # CSRF protection disabled (only for local testing)
SESSION_COOKIE_SECURE = False  # Sessions are not forced to use HTTPS
SECURE_SSL_REDIRECT = False  # Do not redirect HTTP to HTTPS
SECURE_HSTS_SECONDS = 0  # HSTS disabled (not needed for development)
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_CONTENT_TYPE_NOSNIFF = False
