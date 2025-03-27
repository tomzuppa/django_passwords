"""
Views for SecureApp: Handles user authentication, registration, dashboards, logout,
and integrates custom password reset view.
"""

from django.contrib import \
    messages  # Enables user-friendly notification messages
# --------------------------------------------------------
# 🔹 IMPORTS
# --------------------------------------------------------
from django.contrib.auth import logout  # Manages user logout
from django.contrib.auth.decorators import \
    login_required  # Restricts access to logged-in users
from django.contrib.auth.models import User  # Django's built-in User model
from django.contrib.auth.views import \
    PasswordResetView  # Default view for password reset workflow
from django.core.mail import \
    EmailMultiAlternatives  # Used by custom password reset (if needed)
from django.shortcuts import (redirect,  # Renders templates and redirects
                              render)
# Application-specific forms
from secureapp.forms import CreateUserForm, CustomPasswordResetForm


# --------------------------------------------------------
# 🔹 HOME PAGE VIEW
# --------------------------------------------------------
def home(request):
    """
    Renders the landing page or home screen of SecureApp.
    """
    return render(request, "secureapp/index.html")


# --------------------------------------------------------
# 🔹 REGISTRATION VIEW
# --------------------------------------------------------
def register(request):
    """
    Displays a registration form and creates a new user upon valid submission.
    Redirects the user to the 2FA login page upon success.
    """
    # Instantiate an empty registration form
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! Please log in.")
            return redirect("two_factor:login")

    # Pass the form to the template for rendering
    context = {"RegisterForm": form}
    return render(request, "secureapp/register.html", context)


# --------------------------------------------------------
# 🔹 DASHBOARD VIEW (PROTECTED)
# --------------------------------------------------------
@login_required(login_url="two_factor:login")
def dashboard(request):
    """
    Renders a user-specific dashboard page. Only accessible by authenticated users.
    """
    return render(request, "secureapp/dashboard.html")


# --------------------------------------------------------
# 🔹 ACCOUNT LOCKED VIEW
# --------------------------------------------------------
def account_locked(request):
    """
    Renders a warning page when a user's account has been locked due to too many failed login attempts.
    """
    return render(request, "secureapp/account-locked.html")


# --------------------------------------------------------
# 🔹 LOGOUT VIEW
# --------------------------------------------------------
def user_logout(request):
    """
    Logs out the current user and redirects them to the home page with a success message.
    """
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect("home")


# --------------------------------------------------------
# 🔹 CUSTOM PASSWORD RESET VIEW
# --------------------------------------------------------
class CustomPasswordResetView(PasswordResetView):
    """
    Custom Password Reset View that uses CustomPasswordResetForm to avoid duplicate emails
    and to personalize the sender name in outgoing emails.
    """

    form_class = CustomPasswordResetForm
    success_url = "/password_reset_done/"
