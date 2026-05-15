# STA - Système de Traçabilité d’Activité

Application web développée avec Django permettant de centraliser et tracer les activités des développeurs au sein d’une équipe (bugs, sprints, veille, etc.).

---

## Fonctionnalités

- Authentification des utilisateurs (connexion requise)
- Création d’activités (CreateView)
- Consultation détaillée d’une activité (DetailView)
- Modification des activités (UpdateView)
- Suppression sécurisée des activités (DeleteView)
- Classification des activités par catégorie
- Upload et affichage d’images (captures ou preuves)
- Pagination du dashboard
- Sécurité : un utilisateur ne peut modifier ou supprimer que ses propres activités

---

## Stack technique

- Python
- Django
- MySQL
- Bootstrap 5

---

## Modèles principaux

### User
Modèle utilisateur intégré de Django utilisé pour identifier l’auteur des activités.

### Category
- nom : catégorie de l’activité (Bug, Sprint, Veille, etc.)

### Entry
- titre
- contenu
- catégorie (ForeignKey)
- auteur (ForeignKey vers User)
- image (ImageField)
- date de création

---

## Automatisation avec Django Signals

Le projet utilise les Django Signals pour automatiser certaines actions côté backend.

### Fonctionnement

À chaque création d’une nouvelle Entry, un signal Django (`post_save`) est déclenché automatiquement.

Cela permet de :

- détecter la création d’une nouvelle activité
- afficher un log dans le terminal du serveur
- tracer les actions sans intervention manuelle

### Exemple de log

Lorsqu’une activité est créée, le terminal affiche :

[LOG] Entry créée par username le 15/05/2026 à 14:30
---

## Installation du projet

### 1. Cloner le projet
```bash
git clone <url-du-repo>
cd sta-project