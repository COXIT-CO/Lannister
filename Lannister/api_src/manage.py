"""
Django administration utility.
"""
import os
import sys

PWD = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LannisterProject.settings")
    sys.path.append(PWD)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django  # noqa # pylint: disable=unused-import
        except ImportError as error:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from error
        raise
    execute_from_command_line(sys.argv)
