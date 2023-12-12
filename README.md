# DRF ADVANCE TRAINING

A api docs using DRF as a client-side rendering, so not include django.templates

## OS
- Window

## Prerequisites
- Python 3.11
- Virtualenv
- Postgres 14+
- Redis

## Getting started

## virtualenv, migrate and run

```bash
# 1. Create virtual env
python -m venv virtualenv
. virtualenv/Scripts/activate

# 2. Install dependency
pip install -r requirements.txt

# 3. Create .env file
copy ./config/settings/.env.template ./config/settings/.env
# In /config/settings/.env remmeber to config:
#   a. DATABASE_URL
#   b. CELERY_BROKER_URL
#   c. REDIS_CONN_URL

# 4. Migrate database
$ python manage.py migrate

# 5. Start Django
$ python manage.py runserver 0.0.0.0:8000
```

## Create new App

```bash
# 1. Create new app folder
$ mkdir -p apps/[APP_NAME]

# 2. Create new app
$ python manage.py startapp [APP_NAME] apps/[APP_NAME]
```

```python
# 3. Update your app name in app config in apps/[APP_NAME]/apps.py
name = 'apps.[APP_NAME]'

# 4. Add new app in config/settings/common
LOCAL_APPS = (
    'apps.core.apps.CoreConfig',
    'apps.users.apps.UsersConfig',
    'apps.APP_NAME',
)

```

## Addition

```bash
# 1. collect static
python manage.py collectstatic --settings=config.settings.settings --noinput

# 2. create super user
python manage.py createsuperuser
```

## Target

```
An app about forum of blogger
Users: Have basic informations, friends, follower, following, referring_user and contribute point for reward.
Blogs: have basic informations, categories, rate, comments, like and dislike
Users can rating blogs, make friends
```