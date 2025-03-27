"""
🔹 Development settings for Django.

These settings are used when running the project in development mode.
They enable debugging and disable certain security features for ease of development.

⚠️ DO NOT use these settings in production environments!
"""

from .base import *  # Import all shared settings from base.py

# ---------------------------------------------------------
# 🔹 DEBUG MODE (ENABLE ONLY IN DEVELOPMENT)
# ---------------------------------------------------------
DEBUG = (
    True  # Enables detailed error messages for debugging (Never enable in production)
)

# ---------------------------------------------------------
# 🔹 ALLOWED HOSTS (OPEN ACCESS IN DEVELOPMENT)
# ---------------------------------------------------------
ALLOWED_HOSTS = ["*"]  # Accepts all hosts (Useful for local testing)

# ---------------------------------------------------------
# 🔹 DATABASE CONFIGURATION (DEFAULT: SQLITE)
# ---------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Uses SQLite (lightweight, file-based DB)
        "NAME": BASE_DIR / "database/db.sqlite3",  # Database file location
    }
}

# ---------------------------------------------------------
# 🔹 SECURITY SETTINGS (DISABLED FOR DEVELOPMENT)
# ---------------------------------------------------------

# These security settings are disabled in development for testing convenience.
# In production, they should be set to `True` and properly configured.

CSRF_COOKIE_SECURE = (
    False  # Disables CSRF cookie security (unsafe but needed for local testing)
)
SESSION_COOKIE_SECURE = False  # Allows session cookies to be sent over HTTP (unsafe)
SECURE_SSL_REDIRECT = False  # Does not force HTTPS (useful for local development)
SECURE_HSTS_SECONDS = 0  # Disables HTTP Strict Transport Security (HSTS)
SECURE_HSTS_INCLUDE_SUBDOMAINS = False  # No HSTS enforcement for subdomains
SECURE_HSTS_PRELOAD = False  # Disables HSTS preload directive
SECURE_CONTENT_TYPE_NOSNIFF = (
    False  # Allows MIME-type sniffing (not safe but useful for debugging)
)
