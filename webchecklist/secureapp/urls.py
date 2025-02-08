from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import Django's built-in auth views

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
        # Logout (Using Django's built-in LogoutView)
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]
