from django.urls import path
from .views import DashboardView, EntryDetailView
from django.contrib.auth import views as auth_views
from .views import RegisterView
from .forms import LoginForm



urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]