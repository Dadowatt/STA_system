from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Entry
from django.urls import reverse_lazy
from .forms import RegisterForm


class DashboardView(ListView):
    model = Entry
    template_name = 'entries/dashboard.html'
    context_object_name = 'entries'
    ordering = ['date_creation']
    paginate_by = 4


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entries/detail.html'
    context_object_name = 'entry'


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')