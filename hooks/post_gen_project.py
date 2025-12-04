#!/usr/bin/env python
"""
Post-generation hook for cookiecutter-django-backend.

This script runs after the project is generated to:
- Create necessary directories
- Set proper file permissions
"""
import os
import stat


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


if __name__ == '__main__':
    print("\n🚀 Setting up project...")
    make_dirs()
    make_executable()
    print("\n✅ Project setup complete!")
    print("\n📝 Next steps:")
    print("  1. Copy env.example to .env and configure it")
    print("  2. Install dependencies: pip install -r requirements.txt")
    print("  3. Run migrations: python manage.py migrate")
    print("  4. Create superuser: python manage.py createsuperuser")
    print("  5. Start server: python manage.py runserver")
    print("\n")

