from django.shortcuts import render

# home  page
def home(request):
    return render(request, 'index.html')

# register page
def register(request):
    return  render(request, 'register.html')

# dashboard  page
def dashboard(request):
    return render(request, 'dashboard.html')
