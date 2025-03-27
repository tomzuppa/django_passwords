from django.contrib import admin
from django.urls import include, path
from two_factor.urls import \
    urlpatterns as tf_urls  # Import two-factor authentication URLs

# Define the URL patterns for the project
urlpatterns = [
    # Admin site URLs for managing the project
    path("admin/", admin.site.urls),
    # Include URLs from the 'secureapp' application
    path("", include("secureapp.urls")),
    # Include two-factor authentication URLs (from two_factor package)
    path("", include(tf_urls)),
]
