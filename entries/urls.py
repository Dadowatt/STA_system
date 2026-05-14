from django.urls import path
from .views import DashboardView, EntryDetailView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='detail'),
]