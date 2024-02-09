from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .forms import RegistrationForm

app_name = 'account'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>', views.account_activate, name='activate'),
    path('dashboard', views.dashboard, name='dashboard')
]
