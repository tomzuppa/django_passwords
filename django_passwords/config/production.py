"""
Production settings for Django.
These settings are used when the project is deployed in a live environment.
"""

from .base import *  # Import shared settings

# Disable debug mode (NEVER enable DEBUG in production)
DEBUG = False

# Define allowed hosts (update this with your domain or server IP)
ALLOWED_HOSTS = ['your-production-domain.com']

# Secure settings to protect against web attacks
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookie is sent only over HTTPS
SESSION_COOKIE_SECURE = True  # Forces session cookies to use HTTPS
SECURE_SSL_REDIRECT = True  # Redirects HTTP to HTTPS
SECURE_HSTS_SECONDS = 31536000  # Enforces HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Applies HSTS to subdomains
SECURE_HSTS_PRELOAD = True  # Preloads HSTS in browsers
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents browsers from MIME-type sniffing

# Database settings (Use PostgreSQL in production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'your_db_name'),
        'USER': os.getenv('DB_USER', 'your_db_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'your_db_password'),
        'HOST': os.getenv('DB_HOST', 'your_db_host'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
