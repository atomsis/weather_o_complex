import sys

import os
import django
import pytest
from django.conf import settings

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_o_complex.settings")
django.setup()


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        'ATOMIC_REQUESTS': True,

    }
