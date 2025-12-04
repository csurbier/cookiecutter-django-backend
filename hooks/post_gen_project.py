#!/usr/bin/env python
"""
Post-generation hook for cookiecutter-django-backend.

This script runs after the project is generated to:
- Create necessary directories
- Set proper file permissions
- Create Postman collection file
"""
import os
import stat
import json


def make_dirs():
    """Create necessary directories."""
    dirs = [
        'logs',
        'static',
        'media',
    ]
    
    for dir_name in dirs:
        os.makedirs(dir_name, exist_ok=True)
        print(f"✓ Created directory: {dir_name}")


def make_executable():
    """Make manage.py executable."""
    manage_py = 'manage.py'
    if os.path.exists(manage_py):
        st = os.stat(manage_py)
        os.chmod(manage_py, st.st_mode | stat.S_IEXEC)
        print(f"✓ Made {manage_py} executable")


def create_postman_collection():
    """Create Postman collection file with proper variable escaping."""
    # Get cookiecutter context
    import sys
    context_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'cookiecutter.json')
    if os.path.exists(context_file):
        import json as json_module
        with open(context_file, 'r') as f:
            cookiecutter_vars = json_module.load(f)
    else:
        # Fallback: try to get from environment or use defaults
        cookiecutter_vars = {}
    
    # Get actual values from the generated project context
    # These are available in the current directory context
    project_slug = os.path.basename(os.getcwd())
    project_name = project_slug.replace('_', ' ').title()
    
    # Postman collection template with Postman variables properly escaped
    postman_collection = {
        "info": {
            "_postman_id": f"{project_slug}-api-collection",
            "name": f"{project_name} API",
            "description": f"Collection Postman pour tester l'API {project_name}",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "variable": [
            {
                "key": "base_url",
                "value": "http://localhost:8000",
                "type": "string"
            },
            {
                "key": "access_token",
                "value": "",
                "type": "string"
            },
            {
                "key": "refresh_token",
                "value": "",
                "type": "string"
            }
        ],
        "item": [
            {
                "name": "Authentication",
                "item": [
                    {
                        "name": "Create User",
                        "event": [
                            {
                                "listen": "test",
                                "script": {
                                    "exec": [
                                        "if (pm.response.code === 201) {",
                                        "    const response = pm.response.json();",
                                        "    pm.environment.set('user_id', response.id);",
                                        "    pm.environment.set('user_email', response.email);",
                                        "}"
                                    ],
                                    "type": "text/javascript"
                                }
                            }
                        ],
                        "request": {
                            "method": "POST",
                            "header": [
                                {
                                    "key": "Content-Type",
                                    "value": "application/json"
                                }
                            ],
                            "body": {
                                "mode": "raw",
                                "raw": "{\n    \"email\": \"test@example.com\",\n    \"password\": \"testpass123\",\n    \"re_password\": \"testpass123\",\n    \"first_name\": \"Test\",\n    \"last_name\": \"User\"\n}"
                            },
                            "url": {
                                "raw": "{{base_url}}/api/auth/users/",
                                "host": ["{{base_url}}"],
                                "path": ["api", "auth", "users", ""]
                            },
                            "description": "Créer un nouvel utilisateur"
                        },
                        "response": []
                    },
                    {
                        "name": "Get JWT Token",
                        "event": [
                            {
                                "listen": "test",
                                "script": {
                                    "exec": [
                                        "if (pm.response.code === 200) {",
                                        "    const response = pm.response.json();",
                                        "    pm.collectionVariables.set('access_token', response.access);",
                                        "    pm.collectionVariables.set('refresh_token', response.refresh);",
                                        "}"
                                    ],
                                    "type": "text/javascript"
                                }
                            }
                        ],
                        "request": {
                            "method": "POST",
                            "header": [
                                {
                                    "key": "Content-Type",
                                    "value": "application/json"
                                }
                            ],
                            "body": {
                                "mode": "raw",
                                "raw": "{\n    \"email\": \"test@example.com\",\n    \"password\": \"testpass123\"\n}"
                            },
                            "url": {
                                "raw": "{{base_url}}/api/auth/jwt/create/",
                                "host": ["{{base_url}}"],
                                "path": ["api", "auth", "jwt", "create", ""]
                            },
                            "description": "Obtenir un token JWT (access + refresh)"
                        },
                        "response": []
                    },
                    {
                        "name": "Refresh JWT Token",
                        "event": [
                            {
                                "listen": "test",
                                "script": {
                                    "exec": [
                                        "if (pm.response.code === 200) {",
                                        "    const response = pm.response.json();",
                                        "    pm.collectionVariables.set('access_token', response.access);",
                                        "}"
                                    ],
                                    "type": "text/javascript"
                                }
                            }
                        ],
                        "request": {
                            "method": "POST",
                            "header": [
                                {
                                    "key": "Content-Type",
                                    "value": "application/json"
                                }
                            ],
                            "body": {
                                "mode": "raw",
                                "raw": "{\n    \"refresh\": \"{{refresh_token}}\"\n}"
                            },
                            "url": {
                                "raw": "{{base_url}}/api/auth/jwt/refresh/",
                                "host": ["{{base_url}}"],
                                "path": ["api", "auth", "jwt", "refresh", ""]
                            },
                            "description": "Rafraîchir le token JWT (obtenir un nouveau access token)"
                        },
                        "response": []
                    },
                    {
                        "name": "Get Current User (Djoser)",
                        "request": {
                            "method": "GET",
                            "header": [
                                {
                                    "key": "Authorization",
                                    "value": "Bearer {{access_token}}",
                                    "type": "text"
                                }
                            ],
                            "url": {
                                "raw": "{{base_url}}/api/auth/users/me/",
                                "host": ["{{base_url}}"],
                                "path": ["api", "auth", "users", "me", ""]
                            },
                            "description": "Obtenir les informations de l'utilisateur actuel via Djoser"
                        },
                        "response": []
                    },
                    {
                        "name": "Update Current User",
                        "request": {
                            "method": "PATCH",
                            "header": [
                                {
                                    "key": "Authorization",
                                    "value": "Bearer {{access_token}}",
                                    "type": "text"
                                },
                                {
                                    "key": "Content-Type",
                                    "value": "application/json"
                                }
                            ],
                            "body": {
                                "mode": "raw",
                                "raw": "{\n    \"first_name\": \"Updated\",\n    \"last_name\": \"Name\"\n}"
                            },
                            "url": {
                                "raw": "{{base_url}}/api/auth/users/me/",
                                "host": ["{{base_url}}"],
                                "path": ["api", "auth", "users", "me", ""]
                            },
                            "description": "Mettre à jour les informations de l'utilisateur actuel"
                        },
                        "response": []
                    },
                    {
                        "name": "Change Password",
                        "request": {
                            "method": "POST",
                            "header": [
                                {
                                    "key": "Authorization",
                                    "value": "Bearer {{access_token}}",
                                    "type": "text"
                                },
                                {
                                    "key": "Content-Type",
                                    "value": "application/json"
                                }
                            ],
                            "body": {
                                "mode": "raw",
                                "raw": "{\n    \"current_password\": \"testpass123\",\n    \"new_password\": \"newpass123\",\n    \"re_new_password\": \"newpass123\"\n}"
                            },
                            "url": {
                                "raw": "{{base_url}}/api/auth/users/set_password/",
                                "host": ["{{base_url}}"],
                                "path": ["api", "auth", "users", "set_password", ""]
                            },
                            "description": "Changer le mot de passe de l'utilisateur actuel"
                        },
                        "response": []
                    }
                ],
                "description": "Endpoints d'authentification avec Djoser et JWT"
            },
            {
                "name": "Users",
                "item": [
                    {
                        "name": "List Users",
                        "request": {
                            "method": "GET",
                            "header": [
                                {
                                    "key": "Authorization",
                                    "value": "Bearer {{access_token}}",
                                    "type": "text"
                                }
                            ],
                            "url": {
                                "raw": "{{base_url}}/api/users/?page=1",
                                "host": ["{{base_url}}"],
                                "path": ["api", "users", ""],
                                "query": [
                                    {
                                        "key": "page",
                                        "value": "1"
                                    }
                                ]
                            },
                            "description": "Liste paginée de tous les utilisateurs (authentification requise)"
                        },
                        "response": []
                    },
                    {
                        "name": "Get User by ID",
                        "request": {
                            "method": "GET",
                            "header": [
                                {
                                    "key": "Authorization",
                                    "value": "Bearer {{access_token}}",
                                    "type": "text"
                                }
                            ],
                            "url": {
                                "raw": "{{base_url}}/api/users/1/",
                                "host": ["{{base_url}}"],
                                "path": ["api", "users", "1", ""]
                            },
                            "description": "Obtenir les détails d'un utilisateur par son ID"
                        },
                        "response": []
                    },
                    {
                        "name": "Get Current User (Custom Endpoint)",
                        "request": {
                            "method": "GET",
                            "header": [
                                {
                                    "key": "Authorization",
                                    "value": "Bearer {{access_token}}",
                                    "type": "text"
                                }
                            ],
                            "url": {
                                "raw": "{{base_url}}/api/users/me/",
                                "host": ["{{base_url}}"],
                                "path": ["api", "users", "me", ""]
                            },
                            "description": "Obtenir les informations de l'utilisateur actuel via l'endpoint custom"
                        },
                        "response": []
                    }
                ],
                "description": "Endpoints pour gérer les utilisateurs"
            },
            {
                "name": "Alternative Token Endpoints",
                "item": [
                    {
                        "name": "Get Token (Alternative)",
                        "event": [
                            {
                                "listen": "test",
                                "script": {
                                    "exec": [
                                        "if (pm.response.code === 200) {",
                                        "    const response = pm.response.json();",
                                        "    pm.collectionVariables.set('access_token', response.access);",
                                        "    pm.collectionVariables.set('refresh_token', response.refresh);",
                                        "}"
                                    ],
                                    "type": "text/javascript"
                                }
                            }
                        ],
                        "request": {
                            "method": "POST",
                            "header": [
                                {
                                    "key": "Content-Type",
                                    "value": "application/json"
                                }
                            ],
                            "body": {
                                "mode": "raw",
                                "raw": "{\n    \"email\": \"test@example.com\",\n    \"password\": \"testpass123\"\n}"
                            },
                            "url": {
                                "raw": "{{base_url}}/api/token/",
                                "host": ["{{base_url}}"],
                                "path": ["api", "token", ""]
                            },
                            "description": "Alternative endpoint pour obtenir un token JWT"
                        },
                        "response": []
                    },
                    {
                        "name": "Refresh Token (Alternative)",
                        "event": [
                            {
                                "listen": "test",
                                "script": {
                                    "exec": [
                                        "if (pm.response.code === 200) {",
                                        "    const response = pm.response.json();",
                                        "    pm.collectionVariables.set('access_token', response.access);",
                                        "}"
                                    ],
                                    "type": "text/javascript"
                                }
                            }
                        ],
                        "request": {
                            "method": "POST",
                            "header": [
                                {
                                    "key": "Content-Type",
                                    "value": "application/json"
                                }
                            ],
                            "body": {
                                "mode": "raw",
                                "raw": "{\n    \"refresh\": \"{{refresh_token}}\"\n}"
                            },
                            "url": {
                                "raw": "{{base_url}}/api/token/refresh/",
                                "host": ["{{base_url}}"],
                                "path": ["api", "token", "refresh", ""]
                            },
                            "description": "Alternative endpoint pour rafraîchir le token JWT"
                        },
                        "response": []
                    }
                ],
                "description": "Endpoints alternatifs pour les tokens JWT"
            }
        ]
    }
    
    # Write the file
    with open('postman_collection.json', 'w', encoding='utf-8') as f:
        json.dump(postman_collection, f, indent='\t', ensure_ascii=False)
    print("✓ Created postman_collection.json")


if __name__ == '__main__':
    print("\n🚀 Setting up project...")
    make_dirs()
    make_executable()
    create_postman_collection()
    print("\n✅ Project setup complete!")
    print("\n📝 Next steps:")
    print("  1. Copy env.example to .env and configure it")
    print("  2. Install dependencies: pip install -r requirements.txt")
    print("  3. Run migrations: python manage.py migrate")
    print("  4. Create superuser: python manage.py createsuperuser")
    print("  5. Start server: python manage.py runserver")
    print("\n")

