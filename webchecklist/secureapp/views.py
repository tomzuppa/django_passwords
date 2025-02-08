from django.shortcuts import render, redirect  # Import functions to render templates and redirect users
from django.contrib.auth.decorators import login_required  # Protects views from unauthorized access
from .forms import CreateUserForm  # Import the user registration form

# Home Page View
def home(request):
    """
    Handles requests to the home page.
    Renders the 'index.html' template.
    """
    return render(request, 'index.html')

# Register Page View
def register(request):
    """
    Handles user registration by displaying a registration form.
    If a valid form is submitted, it saves the user and redirects to the login page.
    """
    form = CreateUserForm()  # Initialize an empty form
    
    if request.method == 'POST':  # Check if the form is submitted
        form = CreateUserForm(request.POST)  # Populate form with submitted data
        if form.is_valid():  # Validate the form input
            form.save()  # Save the new user to the database
            return redirect('two_factor:login')  # Redirect to the login page for authentication

    context = {'RegisterForm': form}  # Pass the form to the template
    return render(request, 'register.html', context)  # Render the registration page

# Dashboard View (Protected)
@login_required(login_url='two_factor:login')  # Ensures only logged-in users can access the dashboard
def dashboard(request):
    """
    Displays the user dashboard.
    Only accessible to authenticated users.
    """
    return render(request, 'dashboard.html')  # Render the dashboard page
