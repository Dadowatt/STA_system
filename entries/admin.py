from django.contrib import admin
from .models import Entry, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'date_creation')
    search_fields = ('titre', 'contenu')
    list_filter = ('categorie', 'date_creation')