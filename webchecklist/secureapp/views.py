from django.shortcuts import render, redirect
from .forms import CreateUserForm


# home  page
def home(request):
    return render(request, 'index.html')

# Register page view function
def register(request):
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
            
            # Redirect the user to another page after successful registration (placeholder for now)
            return redirect('')  # Add the appropriate URL name or path here

    # Create a context dictionary to pass the form to the template
    context = {'RegisterForm': form}

    # Render the 'register.html' template with the form (empty for GET or filled with user data for POST)
    return render(request, 'register.html', context)

# dashboard  page
def dashboard(request):
    return render(request, 'dashboard.html')
