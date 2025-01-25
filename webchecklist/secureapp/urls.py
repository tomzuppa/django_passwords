from django.urls import path
from . import views  # Import views from the same directory (the dot means "current directory")

# Define URL patterns for the application
urlpatterns = [
    # URL pattern for the home page
    # Maps the root URL ('') to the home view function
    # The name='' is used to refer to this URL in templates or views
    path('', views.home, name='home'),  
    
    # URL pattern for the register page
    # Maps '/register' to the register view function
    # The name='register' allows this URL to be referenced using {% url 'register' %}
    path('register', views.register, name='register'),
    
    # URL pattern for the dashboard page
    # Maps '/dashboard' to the dashboard view function
    # The name='dashboard' allows this URL to be referenced in templates or redirects
    path('dashboard', views.dashboard, name='dashboard'),


    # URL pattern for user logout. 
    # This maps the 'user-logout' URL to the user_logout view function.
    path('user-logout', views.user_logout, name='user-logout'),

]
