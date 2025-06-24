from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view())
    
]
