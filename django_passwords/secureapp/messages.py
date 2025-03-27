from django.contrib import messages  # Django messages framework

#  Success Messages
LOGOUT_SUCCESS = "You have been logged out successfully."
PASSWORD_RESET_SENT = "If the email exists, you will receive a password reset link."
PASSWORD_RESET_SUCCESS = "Your password has been reset successfully."
LOGIN_SUCCESS = "Welcome back!"
REGISTER_SUCCESS = "Your account has been created successfully."
AUTO_LOGOUT_MESSAGE = "The session has expired. Please login again to continue."


#  Error Messages
INVALID_CREDENTIALS = "Invalid email or password. Please try again."
ACCOUNT_LOCKED = "Your account is locked due to multiple failed login attempts."
