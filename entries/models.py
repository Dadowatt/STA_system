from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom


class Entry(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='entries/', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)