from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer

from .models import User


class UserCreateSerializer(BaseUserCreateSerializer):
    """Serializer for creating new users.
    
    Security: Users created via API are never staff or superuser.
    """
    
    def create(self, validated_data):
        """Create a new user, ensuring they are not staff or superuser."""
        # Remove any attempt to set is_staff or is_superuser
        validated_data.pop('is_staff', None)
        validated_data.pop('is_superuser', None)
        # Ensure these are explicitly False
        validated_data['is_staff'] = False
        validated_data['is_superuser'] = False
        return super().create(validated_data)
    
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserSerializer(BaseUserSerializer):
    """Serializer for user data.
    
    Security: is_staff and is_superuser are never exposed or modifiable via API.
    """
    
    def validate(self, attrs):
        """Ensure is_staff and is_superuser cannot be set via API."""
        # Remove any attempt to modify these fields
        attrs.pop('is_staff', None)
        attrs.pop('is_superuser', None)
        return attrs
    
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')
        read_only_fields = ('id', 'date_joined')
        # Explicitly exclude sensitive fields
        extra_kwargs = {
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True},
        }

