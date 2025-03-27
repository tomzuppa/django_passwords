"""
Forms for SecureApp: Handles user creation and custom password reset functionalities.
"""

# --------------------------------------------------------
# 🔹 IMPORTS
# --------------------------------------------------------
from django import forms  # Main forms module from Django
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.contrib.auth.models import \
    User  # Default User model for authentication
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


# --------------------------------------------------------
# 🔹 CREATE USER FORM
# --------------------------------------------------------
class CreateUserForm(UserCreationForm):
    """
    Custom user creation form that extends Django's built-in UserCreationForm.
    This form includes fields for username, email, password1, and password2.
    """

    class Meta:
        # Specify that we are working with Django's built-in User model
        model = User

        # Fields to display in the form for user creation and password confirmation
        fields = ["username", "email", "password1", "password2"]


# --------------------------------------------------------
# 🔹 CUSTOM PASSWORD RESET FORM
# --------------------------------------------------------
# --------------------------------------------------------
# 🔹 CUSTOM PASSWORD RESET FORM
# --------------------------------------------------------
class CustomPasswordResetForm(PasswordResetForm):
    """
    Custom Password Reset Form that checks if the email exists
    and manually sends an email with dynamic timeout context.
    """

    def save(
        self,
        domain_override=None,
        subject_template_name="registration/password_reset_subject.txt",
        email_template_name="registration/password_reset_email.html",
        use_https=False,
        token_generator=default_token_generator,
        request=None,
        *args,
        **kwargs,
    ):

        # Get the current site domain
        current_site = get_current_site(request)

        # Extract the email from the form input
        email = self.cleaned_data["email"]

        # Fetch the user associated with this email (if exists)
        user = User.objects.filter(email=email).first()

        if user:
            # Dynamically fetch timeout value in hours from settings
            timeout_seconds = settings.PASSWORD_RESET_TIMEOUT
            timeout_hours = timeout_seconds // 3600  # Convert seconds to hours

            # Construct the email context
            context = {
                "email": email,
                "domain": domain_override or current_site.domain,
                "site_name": current_site.name,
                "protocol": "https" if request.is_secure() else "http",
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),  # Encode user ID
                "user": user,
                "token": token_generator.make_token(
                    user
                ),  # Generate secure reset token
                "timeout_hours": int(timeout_hours),
            }

            # Render email templates
            subject = render_to_string(subject_template_name, context).strip()
            email_body = render_to_string(email_template_name, context)

            # Construct sender details
            sender_name = settings.EMAIL_SENDER_NAME
            sender_email = settings.DEFAULT_FROM_EMAIL
            full_sender = f"{sender_name} <{sender_email}>"

            # Create and send the email
            email_message = EmailMultiAlternatives(
                subject, email_body, full_sender, [email]
            )
            email_message.send()
