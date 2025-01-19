from django.urls import path
from . import views #point refers that we are in the same directory

urlpatterns = [

      path('', views.home, name='') #home page
    , path('register', views.register, name='register')
    , path('dashboard', views.dashboard, name='dashboard')
]