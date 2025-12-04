"""
Global admin configuration for {{ cookiecutter.project_slug }} project.

All admin registrations should be done here to keep everything centralized.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from axes.admin import AccessAttemptAdmin, AccessLogAdmin
from axes.models import AccessAttempt, AccessLog

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin interface for custom User model."""
    
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'date_joined']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['-date_joined']
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


# Register Axes models for security monitoring
admin.site.register(AccessAttempt, AccessAttemptAdmin)
admin.site.register(AccessLog, AccessLogAdmin)

# Customize admin site
admin.site.site_header = '{{ cookiecutter.project_name }} Administration'
admin.site.site_title = '{{ cookiecutter.project_name }} Admin'
admin.site.index_title = 'Administration'

