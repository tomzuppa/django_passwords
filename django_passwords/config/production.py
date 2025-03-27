"""
🔹 Production settings for Django.

These settings are used when the project is deployed in a live production environment.

⚠️ SECURITY WARNING:
- NEVER enable `DEBUG = True` in production!
- Ensure that all security configurations are properly set.
- Use environment variables to store sensitive credentials.
"""

from .base import *  # Import shared settings from base.py

# ---------------------------------------------------------
# 🔹 DEBUG MODE (MUST BE DISABLED IN PRODUCTION)
# ---------------------------------------------------------
DEBUG = False  # Disables debugging (Avoid exposing error details to users)

# ---------------------------------------------------------
# 🔹 ALLOWED HOSTS (DEFINE YOUR PRODUCTION DOMAIN)
# ---------------------------------------------------------
ALLOWED_HOSTS = [
    "your-production-domain.com"
]  # Replace with your actual domain or server IP

# ---------------------------------------------------------
# 🔹 SECURITY SETTINGS (ENFORCED FOR PRODUCTION)
# ---------------------------------------------------------

CSRF_COOKIE_SECURE = True  # Ensures CSRF token is only transmitted over HTTPS
SESSION_COOKIE_SECURE = True  # Forces session cookies to be transmitted over HTTPS
SECURE_SSL_REDIRECT = True  # Redirects all HTTP requests to HTTPS
SECURE_HSTS_SECONDS = (
    31536000  # Enforces HTTP Strict Transport Security (HSTS) for 1 year
)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Applies HSTS to all subdomains
SECURE_HSTS_PRELOAD = (
    True  # Requests browsers to preload HSTS (Extra layer of security)
)
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME-type sniffing attacks

# ---------------------------------------------------------
# 🔹 DATABASE CONFIGURATION (USE POSTGRESQL IN PRODUCTION)
# ---------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # PostgreSQL is preferred for production
        "NAME": os.getenv(
            "DB_NAME", "your_db_name"
        ),  # Fetch from environment variables
        "USER": os.getenv("DB_USER", "your_db_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "your_db_password"),
        "HOST": os.getenv("DB_HOST", "your_db_host"),
        "PORT": os.getenv("DB_PORT", "5432"),  # Default PostgreSQL port
        "CONN_MAX_AGE": 600,  # Keeps connections alive for 10 minutes (Performance optimization)
    }
}
