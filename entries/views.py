from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry

class DashboardView(ListView):
    model = Entry
    template_name = 'entries/dashboard.html'
    context_object_name = 'entries'
    ordering = ['date_creation']
    paginated_by = 4


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entries/detail.html'
    context_object_name = 'entry'