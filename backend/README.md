# Backend for Typewriter Text Editor

This Django backend is scaffolded and ready for future API and persistence integrations for the typewriter text editor app.

- No endpoints are implemented yet; current persistence is handled client-side (localStorage).
- When backend integration is desired, expose REST endpoints for save/load.

## Setup

This backend uses Django. To get started:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

See the frontend README for the frontend app in `/frontend_app` for details on the UI.
