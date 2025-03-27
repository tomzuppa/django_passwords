from django.contrib.auth import \
    views as auth_views  # Import Django's built-in auth views
from django.urls import path

from . import views
from .views import \
    CustomPasswordResetView  # Import the custom password reset view

# Define URL patterns for the application
urlpatterns = [
    # URL pattern for the home page
    # Maps the root URL ('') to the home view function
    # The name='' is used to refer to this URL in templates or views
    path("", views.home, name="home"),
    # URL pattern for the register page
    # Maps '/register' to the register view function
    # The name='register' allows this URL to be referenced using {% url 'register' %}
    path("register/", views.register, name="register"),
    # URL pattern for the dashboard page
    # Maps '/dashboard' to the dashboard view function
    # The name='dashboard' allows this URL to be referenced in templates or redirects
    path("dashboard/", views.dashboard, name="dashboard"),
    # Use the custom logout function instead of Django's default LogoutView
    path("logout/", views.user_logout, name="logout"),
    # URL pattern for user account-locked
    # Account-locked view
    path("account-locked/", views.account_locked, name="account-locked"),
    # -------------RESET PASSWORD -------------
    # Use our custom view for password reset requests
    path(
        "password_reset/",
        CustomPasswordResetView.as_view(
            template_name="resetPassword/password_reset.html"  # Form where user enters email
        ),
        name="password_reset",
    ),
    # Default views for password reset flow
    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="resetPassword/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="resetPassword/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="resetPassword/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # -----------------------------------------
]
