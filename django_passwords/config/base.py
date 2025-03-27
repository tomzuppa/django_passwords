"""
Base settings for the Django project.

This file contains configurations shared between development and production environments.

- Development-specific settings are in `development.py`
- Production-specific settings are in `production.py`

This structure ensures better security, flexibility, and maintainability.
"""

import os  # Standard library for handling system variables
from datetime import \
    timedelta  # Time handling for configurations (e.g., session expiration)
from pathlib import Path  # Cross-platform file path management

from dotenv import load_dotenv  # Loads environment variables from .env file
from secureapp.messages import \
    AUTO_LOGOUT_MESSAGE  # Custom auto-logout message

# Load environment variables from .env file
load_dotenv()

# ---------------------------------------------------------
# 🔹 BASE DIRECTORY (PROJECT ROOT)
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------
# 🔹 SECURITY SETTINGS
# ---------------------------------------------------------

# Secret key (must be kept private in production)
SECRET_KEY = os.getenv("SECRET_KEY", "change-this-default-key-for-production")

# Debug mode (should be `False` in production)
DEBUG = os.getenv("DEBUG", "False") == "True"  # Converts string 'True' to boolean

# Allowed hosts (prevents host header injection attacks)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")

# ---------------------------------------------------------
# 🔹 INSTALLED APPLICATIONS
# ---------------------------------------------------------
INSTALLED_APPS = [
    # Django Core applications
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # Required for Django’s Sites framework
    "django_extensions",  # Additional management commands for django (pip install django-extensions)
    # Custom applications
    "secureapp.apps.SecureAppConfig",
    # Third-party applications
    "crispy_forms",  # Enhances form styling
    "crispy_bootstrap5",  # Bootstrap 5 support for Crispy Forms
    "django_recaptcha",  # Google reCAPTCHA for security
    "django_otp",  # One-Time Passwords for multi-factor authentication (2FA)
    "django_otp.plugins.otp_static",
    "django_otp.plugins.otp_totp",
    "two_factor",  # Two-Factor Authentication framework
    "axes",  # Protects against brute-force attacks
]

# ---------------------------------------------------------
# 🔹 FORMS & AUTHENTICATION SETTINGS
# ---------------------------------------------------------

# Crispy Forms settings for Bootstrap 5
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Google reCAPTCHA keys (loaded from .env)
RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY", "")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY", "")

# Authentication settings
LOGIN_URL = "two_factor:login"  # Redirect users to 2FA login page
LOGIN_REDIRECT_URL = "dashboard"  # Redirect users after successful login

# ---------------------------------------------------------
# 🔹 SECURITY CONFIGURATIONS
# ---------------------------------------------------------

# Read and process CSRF_TRUSTED_ORIGINS from .env
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]

# Additional security settings
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookies are sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are sent over HTTPS
SECURE_BROWSER_XSS_FILTER = True  # Protects against XSS attacks
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME-type sniffing attacks
SECURE_HSTS_SECONDS = 31536000  # Enforces HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Applies HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Preloads HSTS into browsers for extra security
SECURE_SSL_REDIRECT = True  # Redirects all HTTP requests to HTTPS

# ---------------------------------------------------------
# 🔹 MIDDLEWARE CONFIGURATION
# ---------------------------------------------------------

AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesStandaloneBackend",  # Protects against brute-force attacks
    "django.contrib.auth.backends.ModelBackend",  # Default authentication backend
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_otp.middleware.OTPMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_auto_logout.middleware.auto_logout",
    "axes.middleware.AxesMiddleware",  # Must be placed last
]

# ---------------------------------------------------------
# 🔹 URL & TEMPLATE CONFIGURATION
# ---------------------------------------------------------

ROOT_URLCONF = "project_root.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_auto_logout.context_processors.auto_logout_client",
            ],
        },
    },
]

WSGI_APPLICATION = "project_root.wsgi.application"

# ---------------------------------------------------------
# 🔹 DATABASE CONFIGURATION
# ---------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", BASE_DIR / "database" / "db.sqlite3"),
        "USER": os.getenv("DB_USER", ""),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": os.getenv("DB_PORT", ""),
        "CONN_MAX_AGE": 60,  # Keeps database connections open for 60 seconds
    }
}

# ---------------------------------------------------------
# 🔹 PASSWORD VALIDATION
# ---------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------------------------------------
# 🔹 LOCALIZATION SETTINGS
# ---------------------------------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Mexico_City"
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------
# 🔹 STATIC & MEDIA FILES
# ---------------------------------------------------------

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# MEDIA FILES CONFIGURATION
MEDIA_URL = "/media/"  # URL to access media files in development
MEDIA_ROOT = BASE_DIR / "media"  # Absolute filesystem path where media is stored

# ---------------------------------------------------------
# 🔹 AUTO LOGOUT SETTINGS
# ---------------------------------------------------------

AUTO_LOGOUT = {
    "IDLE_TIME": timedelta(
        minutes=int(os.getenv("AUTO_LOGOUT_MINUTES", 10))
    ),  # minutes
    "REDIRECT_TO_LOGIN_IMMEDIATELY": True,
    "MESSAGE": AUTO_LOGOUT_MESSAGE,
}

# ---------------------------------------------------------
# 🔹 AXES CONFIGURATION (Brute-Force Protection)
# ---------------------------------------------------------

AXES_ENABLED = True
AXES_FAILURE_LIMIT = 3  # Max login attempts before lockout
AXES_COOLOFF_TIME = timedelta(hours=2)  # Cooldown before retrying
AXES_RESET_ON_SUCCESS = True
AXES_LOCKOUT_TEMPLATE = "secureapp/account-locked.html"
AXES_LOCKOUT_PARAMETERS = ["username"]

# ---------------------------------------------------------
# 🔹 EMAIL CONFIGURATION (RESET PASSWORD)
# ---------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_SENDER_NAME = os.getenv("EMAIL_SENDER_NAME", "Default Sender Name")
# Tiempo límite para usar el enlace de reseteo de contraseña (en segundos)
PASSWORD_RESET_TIMEOUT = int(
    os.getenv("PASSWORD_RESET_TIMEOUT", 3600)
)  # por ejemplo, 1 hora


# ---------------------------------------------------------
# 🔹 SITE CONFIGURATION
# ---------------------------------------------------------

SITE_ID = 1
SITE_NAME = os.getenv("DJANGO_SITE_NAME", "Secure X")
SITE_DOMAIN = os.getenv(
    "DJANGO_SITE_DOMAIN",
    "8000-cs-61983882132-default.cs-us-central1-pits.cloudshell.dev",
)
