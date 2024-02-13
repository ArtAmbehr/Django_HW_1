#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Инфо-1."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Инфо-1"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
