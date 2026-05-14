from django.urls import path
from .views import DashboardView, EntryDetailView, EntryUpdateView, EntryCreateView, EntryDeleteView
from django.contrib.auth import views as auth_views
from .views import RegisterView
from .forms import LoginForm



urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
    path('create/', EntryCreateView.as_view(), name='entry-create'),
    path('entry/<int:pk>/update/', EntryUpdateView.as_view(), name='entry-update'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry-delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]