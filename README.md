# STA — Système de Traçabilité d’Activité

**STA** est une application web développée avec **Django** pour centraliser et suivre les activités d'une équipe de développement : corrections de bugs, sprints, veille technologique et autres interventions.

## 1. Fonctionnalités

### Comptes utilisateurs

- Inscription et connexion avec le système d'authentification de Django.
- Déconnexion et gestion des sessions.
- Validation des formulaires et protection CSRF.

### Journal des activités

- **Créer** une activité avec un titre, une description, une catégorie et une image facultative.
- **Consulter** les détails d'une activité.
- **Modifier** ou **supprimer** une activité, avec vérification de son auteur.
- Associer automatiquement l'utilisateur connecté à l'activité créée.
- Afficher les activités par date de création décroissante.

### Organisation et recherche

- Classification par catégories, par exemple **Bug**, **Sprint** et **Veille**.
- Tableau de bord avec recherche par titre, contenu, auteur, catégorie ou identifiant.
- Filtre par catégorie.
- Pagination : **4 activités par page** sur le tableau de bord et **3 activités par page** dans la liste générale.
- Gestion des catégories dans l'interface d'administration Django.

### Traçabilité avec les signaux Django

Un signal `post_save` est déclenché lors de la création d'une activité (`Entry`). Il affiche dans la console du serveur un message indiquant l'auteur et la date.

Exemple :

```text
[LOG] Entry créée par utilisateur123 le 23/11/2026 à 13:30:00+00:00
```

**Important :** il s'agit actuellement d'un message dans le terminal, et non d'un système d'export ou d'archivage permanent des logs.

## 2. Technologies utilisées

| Technologie | Rôle |
| --- | --- |
| **Python** | Logique applicative |
| **Django 6.0.5** | Framework web, authentification et vues basées sur les classes |
| **MySQL** | Stockage des utilisateurs, catégories et activités |
| **HTML / CSS** | Structure et présentation des pages |
| **Bootstrap 5** | Mise en page responsive et composants d'interface |
| **Pillow** | Traitement des fichiers image dans Django |
| **python-dotenv** | Chargement de la configuration depuis un fichier `.env` |

Les versions exactes des dépendances Python sont renseignées dans `requirements.txt`.

## 3. Architecture et modèles

L'application utilise l'architecture de Django, avec des **modèles**, des **formulaires**, des **vues basées sur les classes (CBV)** et des **templates**.

### Modèles de données

| Modèle | Champs / rôle |
| --- | --- |
| **User** | Utilisateur Django, auteur d'une activité |
| **Category** | `nom` : libellé de la catégorie |
| **Entry** | `titre`, `contenu`, `categorie`, `auteur`, `image`, `date_creation` |

**Relations :**

- Un utilisateur peut créer plusieurs activités.
- Une catégorie peut être associée à plusieurs activités.
- Chaque activité possède un auteur et une catégorie.

### Organisation des principaux fichiers

```text
STA_system/
├── config/                 # Configuration générale et routes principales
├── entries/
│   ├── admin.py            # Configuration de l'administration
│   ├── apps.py             # Chargement de l'application et des signaux
│   ├── forms.py            # Formulaires d'inscription et d'activité
│   ├── models.py           # Modèles Category et Entry
│   ├── signals.py          # Log automatique à la création
│   ├── urls.py             # Routes de l'application
│   ├── views.py            # Vues Django basées sur les classes
│   └── templates/          # Pages de connexion, inscription et activités
├── static/css/style.css    # Styles personnalisés
├── templates/base.html     # Structure générale de l'interface
├── .env.example            # Exemple de configuration locale
├── requirements.txt        # Dépendances Python
└── manage.py               # Commandes Django
```

## 4. Installation en local

### Prérequis

- Python et `pip`
- MySQL installé et démarré
- Git

### Étape 1 — Cloner le dépôt

```bash
git clone https://github.com/Dadowatt/STA_system.git
cd STA_system
```

### Étape 2 — Créer et activer un environnement virtuel

**Windows (PowerShell) :**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS :**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Étape 3 — Installer les dépendances

```bash
pip install -r requirements.txt
```

### Étape 4 — Créer une base MySQL

Depuis un client MySQL disposant des droits nécessaires :

```sql
CREATE DATABASE sta_system
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

### Étape 5 — Configurer les variables d'environnement

Créer `.env` à partir de `.env.example`, puis renseigner les valeurs correspondant à votre installation :

```env
DB_NAME=sta_system
DB_USER=votre_utilisateur_mysql
DB_PASSWORD=votre_mot_de_passe_mysql
DB_HOST=127.0.0.1
DB_PORT=3306

SECRET_KEY=votre_cle_secrete_django
DEBUG=True
```

Pour générer une clé secrète Django :

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copier la clé générée dans `SECRET_KEY`. **Ne jamais publier le fichier `.env` ni une véritable clé secrète.** `DEBUG=True` est réservé au développement local.

### Étape 6 — Appliquer les migrations

```bash
python manage.py migrate
```

### Étape 7 — Créer un compte administrateur

```bash
python manage.py createsuperuser
```

### Étape 8 — Démarrer le serveur

```bash
python manage.py runserver
```

Ouvrir ensuite :

- **Application :** http://127.0.0.1:8000/
- **Inscription :** http://127.0.0.1:8000/register/
- **Connexion :** http://127.0.0.1:8000/login/
- **Administration :** http://127.0.0.1:8000/admin/

### Étape 9 — Ajouter les premières catégories

Se connecter à `/admin/`, puis ouvrir **Entries > Categories** pour créer les catégories souhaitées : `Bug`, `Sprint`, `Veille`, etc.

**Remarque :** les migrations créent les tables mais n'importent pas les activités ni les catégories d'une ancienne base de données. Une nouvelle base démarre donc sans données métier.

## 5. Principales routes

| URL | Fonction |
| --- | --- |
| `/` | Tableau de bord, recherche et filtre |
| `/liste/` | Liste des activités |
| `/create/` | Création d'une activité |
| `/entry/<id>/` | Détail d'une activité |
| `/entry/<id>/update/` | Modification d'une activité |
| `/entry/<id>/delete/` | Suppression d'une activité |
| `/categories/` | Liste des catégories |
| `/register/` | Inscription |
| `/login/` | Connexion |
| `/logout/` | Déconnexion (requête POST) |
| `/admin/` | Administration Django |

`<id>` représente l'identifiant numérique d'une activité.

## 6. Sécurité et permissions

Les protections actuellement mises en place comprennent :

- l'authentification Django ;
- le middleware CSRF pour les formulaires ;
- `LoginRequiredMixin` pour le tableau de bord, la création, la modification et la suppression ;
- `UserPassesTestMixin` pour empêcher un utilisateur de modifier ou supprimer une activité dont il n'est pas l'auteur ;
- les validateurs de mots de passe de Django.

**Point restant à corriger :** dans le code publié sur GitHub, les vues de liste générale, de détail et de catégories ne sont pas toutes protégées par `LoginRequiredMixin`. Le projet ne garantit donc pas encore que seules les personnes connectées puissent consulter toutes les pages.

## 7. Limites et améliorations envisagées

- Restreindre l'accès aux pages de liste, de détail et de catégories aux utilisateurs connectés.
- Gérer l'affichage des activités **sans image**, car le champ est facultatif.
- Ajouter un formulaire de création de catégorie directement dans STA, avec des permissions adaptées.
- Renforcer et tester la validation des formulaires.
- Remplacer les textes statiques de certaines pages par les véritables données des activités.
- Rendre fonctionnel le bouton « Exporter les logs » (actuellement présent dans l'interface sans fonctionnalité associée).
- Ajouter des tests automatisés pour les droits d'accès et les opérations CRUD.
- Mettre en place un stockage durable des journaux d'activité si un audit permanent est nécessaire.

Les messages affichés dans l'interface à propos de notifications aux superviseurs ne correspondent pas encore à un système de notification implémenté.

## Développé par

**Dado Watt**  
Développeuse Web, Web Mobile et IA  

Projet individuel réalisé dans le cadre de la formation Simplon Sénégal.  

