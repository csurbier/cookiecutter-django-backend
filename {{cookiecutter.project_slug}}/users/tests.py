"""
Tests for users app.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):
    """Test cases for User model."""
    
    def test_create_user_with_email(self):
        """Test creating a user with email."""
        email = 'test@example.com'
        password = 'testpass123'
        user = User.objects.create_user(email=email, password=password)
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        """Test creating a superuser."""
        email = 'admin@example.com'
        password = 'adminpass123'
        user = User.objects.create_superuser(email=email, password=password)
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
    
    def test_user_email_normalized(self):
        """Test that email is normalized."""
        email = 'test@EXAMPLE.COM'
        user = User.objects.create_user(email=email, password='test123')
        
        self.assertEqual(user.email, email.lower())
    
    def test_user_str_representation(self):
        """Test user string representation."""
        email = 'test@example.com'
        user = User.objects.create_user(email=email, password='test123')
        
        self.assertEqual(str(user), email)
    
    def test_user_get_full_name(self):
        """Test user get_full_name method."""
        email = 'test@example.com'
        user = User.objects.create_user(
            email=email,
            password='test123',
            first_name='John',
            last_name='Doe'
        )
        
        self.assertEqual(user.get_full_name(), 'John Doe')
        
        # Test without first/last name
        user2 = User.objects.create_user(email='test2@example.com', password='test123')
        self.assertEqual(user2.get_full_name(), 'test2@example.com')

