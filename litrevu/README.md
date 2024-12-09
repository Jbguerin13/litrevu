
# LITReview : Projet d'école [openclassroom](https://openclassrooms.com/fr) est une Application web pour la gestion des critiques littéraires

LITReview est une application web permettant de créer, visualiser et répondre à des critiques littéraires sous forme de tickets et de reviews. Ce projet est conçu pour être exécuté localement dans un environnement Django.

## Installation et exécution

Suivez les étapes ci-dessous pour installer et exécuter le projet LITReview localement.

### Prérequis

- Python 3.9 ou version ultérieure
- pip (gestionnaire de paquets Python)
- Un environnement de développement intégré (IDE) comme VSCode ou PyCharm (optionnel)

### Étapes d'installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/Jbguerin13/litrevu
   cd LITReview
   ```

2. **Créer un environnement virtuel** :
   Sous Windows :
   ```bash
   python -m venv env
   env\Scripts\activate
   ```
   Sous macOS/Linux :
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations de la base de données** :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Créer un superutilisateur** (optionnel pour accéder à l'interface d'administration) :
   ```bash
   python manage.py createsuperuser
   ```

6. **Lancer le serveur** :
   ```bash
   python manage.py runserver
   ```

7. **Accéder à l'application** :
   - Application principale : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Interface d'administration : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Étapes pour les lancements ultérieurs

- Activez votre environnement virtuel :
  ```bash
  env\Scripts\activate  # Windows
  source env/bin/activate  # macOS/Linux
  ```
- Lancez le serveur :
  ```bash
  python manage.py runserver
  ```

---

## Fonctionnalités principales

### Gestion des tickets et critiques
- **Créer un ticket** : Demandez une critique pour un livre ou un article.
- **Répondre à un ticket** : Rédigez une critique en réponse à un ticket existant.

### Flux d'activités
- **Voir les publications des utilisateurs suivis** : Accédez aux tickets et critiques des utilisateurs que vous suivez.

### Gestion personnelle
- **Gérez vos propres publications** : Visualisez, modifiez ou supprimez vos tickets et critiques depuis la section "Vos posts".

### Système de suivi
- **Suivre d'autres utilisateurs** : Personnalisez votre flux en suivant les utilisateurs de votre choix.

---

## Conformité avec le cahier des charges

1. **Instructions pour configuration locale** :
   - Les étapes ci-dessus permettent une configuration complète de l'application en local.

2. **Fonctionnalités conformes** :
   - Création, gestion et affichage des tickets et critiques.
   - Flux d'activités regroupant les publications des utilisateurs suivis.
   - Gestion des abonnements.

3. **Wireframes respectés** :
   - L'interface utilisateur respecte les wireframes avec des ajustements esthétiques pour une meilleure expérience utilisateur.

---

## Structure du projet

Voici la structure principale du projet Django :
```
LITReview/
├── authentification/         # Gestion des utilisateurs
├── review/                   # Gestion des tickets, critiques et abonnements
├── static/                   # Fichiers CSS, JS et images
├── templates/                # Fichiers HTML
├── manage.py                 # Point d'entrée du projet
├── requirements.txt          # Dépendances Python
└── db.sqlite3                # Base de données locale (générée après migration)
```

---