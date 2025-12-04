# Django
export SECRET_KEY=rtfgyour-secret-key-here-change-in-production
export DEBUG=True
export ALLOWED_HOSTS=localhost,127.0.0.1
export STATIC_URL_PREFIX=/static
export MEDIA_URL_PREFIX=/media
export APP_HOME=
# Database - PostgreSQL
export DATABASE_NAME=your_db_name
export DATABASE_USER=your_db_user
export DATABASE_PASSWORD=your_db_password
export DATABASE_HOST=localhost
export DATABASE_PORT=5432

# Redis

export REDIS_URL=redis://localhost:6379/0
export REDIS_CACHE_URL=redis://localhost:6379/1


# Celery

export CELERY_BROKER_URL=redis://localhost:6379/0
export CELERY_RESULT_BACKEND=redis://localhost:6379/0


# Email (optional)
export EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
export EMAIL_HOST=smtp.gmail.com
export EMAIL_PORT=587
export EMAIL_USE_TLS=True
export EMAIL_HOST_USER=
export EMAIL_HOST_PASSWORD=

# JWT
export JWT_SECRET_KEY=your-jwt-secret-key-here
export JWT_ALGORITHM=HS256
export JWT_ACCESS_TOKEN_LIFETIME=60
export JWT_REFRESH_TOKEN_LIFETIME=1440
