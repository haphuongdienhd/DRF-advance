from .common import *
from .common import INSTALLED_APPS, MIDDLEWARE, TEMPLATES, env

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool("DJANGO_DEBUG", default=True)
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG
ALLOWED_HOSTS = ["*"]


# django-debug-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += ("debug_toolbar",)
MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

INTERNAL_IPS = [
    "127.0.0.1",
    "10.0.2.2",
]

# django-extensions & nose test
# ------------------------------------------------------------------------------
INSTALLED_APPS += ("django_extensions",)
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=["http://*", "https://*"])