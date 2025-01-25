# Import the default UserCreationForm provided by Django
# This form includes fields for creating a new user with password validation
from django.contrib.auth.forms import UserCreationForm

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
