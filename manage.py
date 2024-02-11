#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# importing base directory path
from dashboard.settings import BASE_DIR


def main():
    # creating required folders folders for model and uploaded text files
    if 'uploads' not in os.listdir(BASE_DIR):
        os.mkdir(BASE_DIR / 'uploads')
    if 'embedding_model' not in os.listdir(BASE_DIR):
        os.mkdir(BASE_DIR / 'embedding_model')
    
    """Run administrative tasks."""
    # switching between local and server settings based on environment variable
    settings_module = 'dashboard.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'dashboard.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
