"""
Base settings for Django project.

This file contains common configurations that are shared across development 
and production environments. 

- Development-specific settings are in `development.py`
- Production-specific settings are in `production.py`

This structure allows for better security and flexibility when deploying Django applications.
"""

from pathlib import Path  # Used to manage file paths in a cross-platform way
from datetime import timedelta  # Handles time-based settings (e.g., session expiration)
from dotenv import load_dotenv  # Loads environment variables from .env file
import os  # Standard library for interacting with the operating system

# Load environment variables from .env file
load_dotenv()

# 1️⃣ BASE DIRECTORY (PROJECT ROOT)
# Defines the absolute path to the project's root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 2️⃣ SECURITY SETTINGS

# SECRET_KEY: Critical for cryptographic signing, should be kept secret in production
SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-default-key-for-production')

# DEBUG MODE: Enables debugging features (only use `True` in development!)
DEBUG = os.getenv('DEBUG', 'False') == 'True'  # Converts string 'True' to boolean

# ALLOWED HOSTS: Defines which domains/hosts can serve this Django app
# Example: 'yourwebsite.com,www.yourwebsite.com' → ['yourwebsite.com', 'www.yourwebsite.com']
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# 3️⃣ INSTALLED APPLICATIONS

INSTALLED_APPS = [
    # Default Django apps required for core functionalities
    'django.contrib.admin',  # Django Admin interface
    'django.contrib.auth',  # Authentication system
    'django.contrib.contenttypes',  # Content types framework
    'django.contrib.sessions',  # Manages user sessions
    'django.contrib.messages',  # Enables message framework
    'django.contrib.staticfiles',  # Handles static files (CSS, JavaScript, Images)

    # Your custom application (main app of the project)
    'secureapp',  

    # Third-party applications
    'crispy_forms',  # Enhances Django forms styling
    'crispy_bootstrap5',  # Bootstrap 5 support for Crispy Forms
    'django_recaptcha',  # Google reCAPTCHA for security
    'django_otp',  # One-Time Passwords for multi-factor authentication
    'django_otp.plugins.otp_static',  # Static OTP support for 2FA
    'django_otp.plugins.otp_totp',  # Time-based OTP support (like Google Authenticator)
    'two_factor',  # Two-Factor Authentication framework
]

# 4️⃣ FORMS & AUTHENTICATION

# Crispy Forms settings for Bootstrap 5
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Google reCAPTCHA keys (loaded from .env)
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY', '')

# Authentication settings
LOGIN_URL = 'two_factor:login'  # Redirect users to 2FA login page
LOGIN_REDIRECT_URL = 'dashboard'  # Redirect users after successful login

# 5️⃣ SECURITY SETTINGS

# CSRF Protection: Defines trusted domains for Cross-Site Request Forgery protection
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', '').split(',')

# Additional security settings for Django
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookies are sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are sent over HTTPS
SECURE_BROWSER_XSS_FILTER = True  # Protects against XSS attacks in modern browsers
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME-type sniffing security risk
SECURE_HSTS_SECONDS = 31536000  # Enforces HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Applies HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Preloads HSTS into browsers for additional security
SECURE_SSL_REDIRECT = True  # Redirects all HTTP requests to HTTPS

# 6️⃣ MIDDLEWARE CONFIGURATION
# Middleware are functions that process requests before they reach the views

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Provides security enhancements
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manages user sessions
    'django.middleware.common.CommonMiddleware',  # Common utilities like URL rewriting
    'django.middleware.csrf.CsrfViewMiddleware',  # Enables CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Handles authentication
    'django_otp.middleware.OTPMiddleware',  # Enables two-factor authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Manages flash messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevents clickjacking
    'django_auto_logout.middleware.auto_logout',  # Enables automatic logout for inactivity
]

# 7️⃣ URL & TEMPLATE CONFIGURATION

ROOT_URLCONF = 'project_root.urls'  # Defines the root URL configuration

# Template settings (HTML rendering engine)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Looks for custom templates in /templates/
        'APP_DIRS': True,  # Automatically loads templates from installed apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for Crispy Forms
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_auto_logout.context_processors.auto_logout_client',  # Auto logout handler
            ],
        },
    },
]

# 8️⃣ WSGI APPLICATION (For running the project with a WSGI server)
WSGI_APPLICATION = 'project_root.wsgi.application'

# 9️⃣ DATABASE CONFIGURATION (Uses environment variables for security)
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DB_NAME', BASE_DIR / 'database' / 'db.sqlite3'),
        'USER': os.getenv('DB_USER', ''),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', ''),
    }
}

# 🔟 PASSWORD VALIDATION

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🔟.1 LOCALIZATION SETTINGS

LANGUAGE_CODE = 'en-us'  # Default language for the app
TIME_ZONE = 'America/Mexico_City'  # Time zone setting
USE_I18N = True  # Enables internationalization
USE_TZ = True  # Enables timezone support

# 🔟.2 STATIC & MEDIA FILES

STATIC_URL = '/static/'  # URL path for static files
STATICFILES_DIRS = [BASE_DIR / 'static']  # Location where static files are stored

# 🔟.3 AUTO LOGOUT SETTINGS
# Automatically logs out users after a period of inactivity
AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=int(os.getenv('AUTO_LOGOUT_MINUTES', 5))),  # Default: 5 min
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
}
