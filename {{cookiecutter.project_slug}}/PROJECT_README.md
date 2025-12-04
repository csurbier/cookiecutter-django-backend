# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Caractéristiques

- ✅ **Modèle User personnalisé** : Authentification par email (pas de username)
- ✅ **Djoser** : Authentification API complète avec JWT
- ✅ **Django REST Framework** : API RESTful
- ✅ **Documentation Swagger/OpenAPI** : Documentation interactive protégée (drf-spectacular)
- ✅ **Django Axes** : Protection contre les attaques brute force sur l'admin
- ✅ **Redis** : Cache et broker pour Celery
- ✅ **Celery** : Traitements asynchrones

## Prérequis

- Python {{ cookiecutter.python_version }}
- PostgreSQL
{% if cookiecutter.use_redis == "yes" %}
- Redis
{% endif %}
- pip et virtualenv (ou venv)

## Installation

1. **Créer un environnement virtuel** :

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

2. **Installer les dépendances** :

```bash
pip install -r requirements.txt
```

3. **Configurer les variables d'environnement** :

```bash
cp env.example .env
# Éditer .env avec vos valeurs (notamment les paramètres PostgreSQL)
```

4. **Créer la base de données PostgreSQL** :

```bash
createdb your_db_name
# Ou via psql: CREATE DATABASE your_db_name;
```

5. **Appliquer les migrations** :

```bash
python manage.py migrate
```

6. **Créer un superutilisateur** :

```bash
python manage.py createsuperuser
# Utiliser votre email comme identifiant (pas de username)
```

7. **Démarrer le serveur de développement** :

```bash
python manage.py runserver
```

{% if cookiecutter.use_celery == "yes" %}
## Celery

Pour démarrer le worker Celery :

```bash
celery -A {{ cookiecutter.project_slug }} worker -l info
```

Pour démarrer Celery Beat (tâches périodiques) :

```bash
celery -A {{ cookiecutter.project_slug }} beat -l info
```
{% endif %}

## Structure du projet

```
{{ cookiecutter.project_slug }}/
├── manage.py
├── requirements.txt
├── postman_collection.json  # Collection Postman pour tester l'API
├── {{ cookiecutter.project_slug }}/
│   ├── settings/
│   │   ├── base.py          # Configuration de base
│   │   ├── development.py   # Configuration développement
│   │   └── production.py    # Configuration production
│   ├── urls.py
│   ├── views.py             # Vues pour la documentation Swagger (protégée)
│   ├── admin.py             # Configuration admin globale (centralisée)
│   ├── wsgi.py
│   ├── asgi.py
│   └── celery.py            # Configuration Celery
└── users/
    ├── models.py            # Modèle User personnalisé
    ├── serializers.py       # Serializers Djoser
    ├── views.py             # ViewSets API
    └── admin.py             # Vide (admin centralisé dans {{ cookiecutter.project_slug }}/admin.py)
```

## API Endpoints

### Authentification (Djoser)

- `POST /api/auth/users/` - Créer un utilisateur
- `GET /api/auth/users/me/` - Obtenir les informations de l'utilisateur actuel
- `PATCH /api/auth/users/me/` - Mettre à jour l'utilisateur actuel
- `POST /api/auth/users/set_password/` - Changer le mot de passe
- `POST /api/auth/jwt/create/` - Obtenir un token JWT
- `POST /api/auth/jwt/refresh/` - Rafraîchir un token JWT

### Utilisateurs

- `GET /api/users/` - Liste des utilisateurs (authentifié requis)
- `GET /api/users/{id}/` - Détails d'un utilisateur
- `GET /api/users/me/` - Informations de l'utilisateur actuel

### Collection Postman

Une collection Postman complète est fournie dans `postman_collection.json` pour tester tous les endpoints.

**Pour importer dans Postman :**
1. Ouvrir Postman
2. Cliquer sur "Import"
3. Sélectionner le fichier `postman_collection.json`
4. La collection sera importée avec toutes les requêtes pré-configurées

**Variables de la collection :**
- `base_url` : URL de base de l'API (par défaut: http://localhost:8000)
- `access_token` : Token JWT d'accès (rempli automatiquement après connexion)
- `refresh_token` : Token JWT de rafraîchissement (rempli automatiquement après connexion)

Les tokens sont automatiquement sauvegardés dans les variables de collection après les requêtes d'authentification.

### Documentation API (Swagger/OpenAPI)

La documentation interactive de l'API est disponible via Swagger UI et ReDoc. **L'accès est protégé et nécessite une authentification.**

**Endpoints de documentation :**
- `GET /api/schema/` - Schéma OpenAPI (JSON/YAML)
- `GET /api/docs/` - Interface Swagger UI (interactive)
- `GET /api/redoc/` - Interface ReDoc (alternative)

**Pour accéder à la documentation :**

1. **Obtenir un token JWT** (voir section Authentification ci-dessus)
2. **Accéder à Swagger UI** :
   - Ouvrir `http://localhost:8000/api/docs/` dans votre navigateur
   - Cliquer sur le bouton "Authorize" en haut à droite
   - Entrer : `Bearer <votre_access_token>`
   - Cliquer sur "Authorize" puis "Close"
   - Vous pouvez maintenant explorer et tester l'API directement depuis Swagger

**Alternative avec ReDoc :**
- Ouvrir `http://localhost:8000/api/redoc/`
- L'authentification se fait via le header `Authorization: Bearer <token>`

La documentation est générée automatiquement à partir de vos serializers, views et modèles Django REST Framework.

## Sécurité

- **Django Axes** : Protège l'interface admin contre les attaques brute force
- **JWT Authentication** : Tokens sécurisés pour l'API
- **CORS** : Configuration pour les requêtes cross-origin
- **Settings de production** : Configuration sécurisée pour la production

## Développement

Pour utiliser les settings de développement :

```bash
export DJANGO_SETTINGS_MODULE={{ cookiecutter.project_slug }}.settings.development
python manage.py runserver
```

Ou modifier `manage.py` pour utiliser `settings.development` par défaut.

## Auteur

{{ cookiecutter.author_name }} - {{ cookiecutter.author_email }}

