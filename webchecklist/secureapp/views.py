from django.shortcuts import render, redirect
from .forms import CreateUserForm  # Import the custom user creation form
from django.contrib.auths.models import auth # Importing the auth module from django.contrib.auths.models, which provides authentication functionality.
from django.contrib.auth.decorators import login_required # Importing the login_required decorator from django.contrib.auth.decorators, which ensures that a user is authenticated before accessing a view.

# Home page view function
def home(request):
    """
    Handles requests to the home page.
    Renders the 'index.html' template for the home page.
    """
    return render(request, 'index.html')

# Register page view function
def register(request):
    """
    Handles user registration. Renders a form for user creation
    and processes the form submission to create a new user.
    """
    # Create an instance of the CreateUserForm (empty form for GET requests)
    form = CreateUserForm()
    
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Populate the form with the data submitted by the user
        form = CreateUserForm(request.POST)
        
        # Check if the submitted form data is valid
        if form.is_valid():
            # Save the form data to create a new user in the database
            form.save()
            
            # Redirect the user to the login page for two-factor authentication
            return redirect('two_factor:login')  # Redirect to the two-factor authentication login page

    # Create a context dictionary to pass the form to the template
    context = {'RegisterForm': form}

    # Render the 'register.html' template with the form (empty for GET or filled with user data for POST)
    return render(request, 'register.html', context)

# Dashboard page view function

# This decorator ensures that the user must be logged in to access the decorated view.
# If the user is not authenticated, they will be redirected to the specified login URL.
@login_required(login_url='two_factor:login')
def dashboard(request):
    """
    Handles requests to the dashboard page.
    Renders the 'dashboard.html' template for authenticated users.
    """
    return render(request, 'dashboard.html')


def user_logout(request):
    # This function logs out the current user and redirects them to the homepage.
    auth.logout(request)
    return redirect('')