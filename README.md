# Cookiecutter Django Backend

Un template cookiecutter pour générer rapidement un backend Django avec :

- ✅ Modèle User personnalisé avec email comme identifiant
- ✅ Authentification API avec Djoser
- ✅ Backoffice admin sécurisé avec django-axes (protection brute force)
- ✅ Django REST Framework pour l'API
- ✅ Documentation Swagger/OpenAPI protégée (drf-spectacular)
- ✅ Collection Postman prête à l'emploi
- ✅ Redis pour le cache
- ✅ Celery pour les traitements asynchrones

## Utilisation

```bash
cookiecutter /path/to/cookiecutter-django-backend
```

Ou depuis GitHub :

```bash
cookiecutter gh:yourusername/cookiecutter-django-backend
```

## Structure du projet généré

Le projet généré inclut :

- Configuration Django modulaire (settings/)
- Application `users` avec modèle User personnalisé
- Configuration Djoser pour l'authentification API
- Configuration django-axes pour la sécurité admin
- Documentation Swagger/OpenAPI protégée
- Collection Postman pour tester l'API
- Configuration Redis et Celery
- Fichiers de configuration (env.example, etc.)
- Requirements.txt avec toutes les dépendances
- Base de données PostgreSQL

## Variables du template

Lors de la génération, vous serez invité à renseigner :

- `project_name` : Nom du projet
- `author_name` : Nom de l'auteur
- `author_email` : Email de l'auteur
- `django_version` : Version de Django (par défaut: 5.0)
- `python_version` : Version de Python (par défaut: 3.12)
- `use_redis` : Utiliser Redis (yes/no)
- `use_celery` : Utiliser Celery (yes/no)
- `timezone` : Fuseau horaire
- `language_code` : Code de langue

