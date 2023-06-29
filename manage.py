#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading

from django.core.management import execute_from_command_line

from netsec.telegram_bot_handler import start_telegram_bot


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websec.settings')
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
    # Start the Telegram bot in a separate thread
    bot_thread = threading.Thread(target=start_telegram_bot)
    bot_thread.start()

    # Run the Django development server
    main()

