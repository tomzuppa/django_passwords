from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import Django's built-in auth views
from secureapp.forms import CustomPasswordResetForm  # Import our custom form




# Define URL patterns for the application
urlpatterns = [
    # URL pattern for the home page
    # Maps the root URL ('') to the home view function
    # The name='' is used to refer to this URL in templates or views
    path('', views.home, name='home'),  
    
    # URL pattern for the register page
    # Maps '/register' to the register view function
    # The name='register' allows this URL to be referenced using {% url 'register' %}
    path('register/', views.register, name='register'),
    
    # URL pattern for the dashboard page
    # Maps '/dashboard' to the dashboard view function
    # The name='dashboard' allows this URL to be referenced in templates or redirects
    path('dashboard/', views.dashboard, name='dashboard'),


    # URL pattern for user logout. 
        # Logout (Using Django's built-in LogoutView)
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # URL pattern for user account-locked
    # Account-locked view
    path('account-locked/', views.accountLocked, name='account-locked'),



    #-------------RESET PASSWORD -------------
    
        # 🔒 Password Reset using our custom form (only checks email)
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='resetPassword/password_reset.html',  # Updated path
        form_class=CustomPasswordResetForm  # Use the custom form here
    ), name='password_reset'),

    # Password Reset Done (Confirmation that email was sent)
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='resetPassword/password_reset_done.html'  # Updated path
    ), name='password_reset_done'),

    # Password Reset Confirm (Page where user enters new password)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='resetPassword/password_reset_confirm.html'  # Updated path
    ), name='password_reset_confirm'),

    # Password Reset Complete (Success message after reset)
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='resetPassword/password_reset_complete.html'  # Updated path
    ), name='password_reset_complete'),

    #-----------------------------------------

]
