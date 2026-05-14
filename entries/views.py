from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Entry
from django.urls import reverse_lazy
from .forms import RegisterForm, EntryForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class DashboardView(ListView):
    model = Entry
    template_name = 'entries/dashboard.html'
    context_object_name = 'entries'
    ordering = ['-date_creation']
    paginate_by = 4


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entries/detail.html'
    context_object_name = 'entry'


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entries/create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)
    

class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entries/update.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        entry = self.get_object()
        return self.request.user == entry.auteur
    

class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    template_name = 'entries/delete.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        entry = self.get_object()
        return self.request.user == entry.auteur