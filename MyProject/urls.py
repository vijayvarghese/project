from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    # Add more paths as needed
]
