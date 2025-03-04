# Import the default UserCreationForm provided by Django
# This form includes fields for creating a new user with password validation
from django.contrib.auth.forms import UserCreationForm

# Import the 'forms' module from Django. This module is used for creating and handling forms.
from django import forms
# Import the 'PasswordResetForm' class from Django's authentication forms. This form is used to handle the password reset process.
from django.contrib.auth.forms import PasswordResetForm
# Import the 'User' model from Django's authentication models. This model is used to represent users in the system.
from django.contrib.auth.models import User


# Import the default User model provided by Django
# The User model handles authentication and stores user data (e.g., username, email, password)
from django.contrib.auth.models import User

# Custom user creation form extending the default UserCreationForm
class CreateUserForm(UserCreationForm):
    """
    A custom user creation form that extends Django's built-in UserCreationForm.
    This form allows creating new users with the specified fields: username, email, password1, and password2.
    """
    class Meta:
        # Specifies the model the form will use (Django's built-in User model)
        model = User

        # Fields to include in the form
        # 'password1' and 'password2' are for password creation and confirmation
        fields = ['username', 'email', 'password1', 'password2']



#---- RESET PASSWORD ------------------
class CustomPasswordResetForm(PasswordResetForm):
    """
    Custom Password Reset Form that checks if the email exists.
    This form extends Django's built-in PasswordResetForm to provide custom validation.
    """
    email = forms.EmailField(label="Email", max_length=254)
    # Define the email field, which is required for password reset.
    # `label="Email"` sets the label of the field in the rendered form.
    # `max_length=254` sets the maximum allowed length for the email address.

    def clean_email(self):
        """
        Validate that the entered email exists in the system.
        If not, still return success message for security reasons.
        This method overrides the default email validation to add a custom check.
        """
        email = self.cleaned_data.get("email")
        # Retrieve the email address from the form's cleaned data.
        # `cleaned_data` is a dictionary of the validated and cleaned form data.

        users = User.objects.filter(email=email)
        # Query the User model to check if any user exists with the provided email.
        # `User.objects.filter(email=email)` performs a lookup in the database.

        if not users.exists():
            # Check if the query returned any results (i.e., if a user with that email exists).
            # If `users.exists()` returns False, it means no user with that email was found.

            # We won't raise an error, just proceed as normal to avoid exposing user emails
            # This is a security measure to prevent attackers from enumerating valid user email addresses.
            return email  # Still return the input value to avoid form errors
            # Even if no user was found, we return the email address without raising an error.
            # This prevents the form from showing an error message and potentially revealing
            # whether an email is registered or not.

        return email
        # If a user with the provided email was found, return the email address.
        # This indicates that the email is valid.

#-------------------------------------------