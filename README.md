# Book Catalog

Django REST API for a book catalog — Dev Ops course work 2026.

## What's been done

1. **Python virtual environment** created with `python -m venv .venv` for isolated dependencies
2. **Django** and **Django REST Framework** installed via pip
3. **Django project** scaffolded with `django-admin startproject bookcatalog ./`
4. **SQLite database** migrated (`python manage.py migrate`)
5. **API app** created with `python manage.py startapp api`
6. **`rest_framework` and `api`** registered in `INSTALLED_APPS` in `settings.py`

*Next: define models, serializers, views, and API endpoints.*

## Setup

```bash
git clone <repo-url>
cd work1
python -m venv .venv
source .venv/bin/activate
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

## Project structure

```
├── bookcatalog/              # Django project container
│   ├── __init__.py           # Marks this as a Python package
│   ├── settings.py           # All project config: installed apps, DB, middleware, templates
│   ├── urls.py               # Root URL dispatcher — maps incoming URLs to views
│   ├── wsgi.py               # Entry point for WSGI-compatible servers (production)
│   └── asgi.py               # Entry point for ASGI-compatible servers (async)
├── api/                      # Reusable Django app for the book catalog API
│   ├── __init__.py
│   ├── admin.py              # Register models here to manage via Django admin panel
│   ├── apps.py               # App configuration (auto-generated)
│   ├── models.py             # Define database tables as Python classes
│   ├── views.py              # Handle HTTP requests and return responses
│   ├── tests.py              # Unit tests for the app
│   ├── serializers.py        # (to create) DRF serializers — convert model data to/from JSON
│   └── migrations/           # Auto-generated DB schema change history
├── manage.py                 # Django's CLI tool — runserver, migrate, startapp, etc.
├── db.sqlite3                # SQLite database file (auto-created, not committed)
├── .venv/                    # Python virtual environment with installed packages
└── .gitignore                # Files Git should ignore (venv, db, cache, etc.)
```
