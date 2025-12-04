"""
Views for {{ cookiecutter.project_slug }} project.
"""
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.permissions import IsAuthenticated


class ProtectedSpectacularAPIView(SpectacularAPIView):
    """Protected API schema view - requires authentication."""
    permission_classes = [IsAuthenticated]


class ProtectedSpectacularSwaggerView(SpectacularSwaggerView):
    """Protected Swagger UI view - requires authentication."""
    permission_classes = [IsAuthenticated]


class ProtectedSpectacularRedocView(SpectacularRedocView):
    """Protected ReDoc view - requires authentication."""
    permission_classes = [IsAuthenticated]

