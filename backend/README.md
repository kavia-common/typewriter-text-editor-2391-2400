# Backend for Typewriter Text Editor

This Django backend hosts API endpoints for the typewriter text editor app.

## Available Endpoints

- `GET /api/health/` — Health check, returns `{ "status": "ok" }`.
- `POST /api/texts/` — Save a text blob with metadata. Payload: `{ "title": str, "text": str, "updated_at"?: str (ISO) }`.
- `GET /api/texts/` — List all saved text entries (`id`, `title`, `updated_at`).
- `GET /api/texts/{id}/` — Fetch a single text entry.
- `DELETE /api/texts/{id}/` — Delete a saved entry.

Text persistence is "local-first", using a simple file-based store in `backend/texts_storage/` (no migrations needed).

CORS is enabled to allow requests from the frontend app (uses `REACT_APP_FRONTEND_URL` if set, otherwise allows `http://localhost:3000`).

## Setup

This backend uses Django. To get started:

```bash
pip install -r requirements.txt
python manage.py runserver 3001
```

You do NOT need to run migrations for text persistence.
