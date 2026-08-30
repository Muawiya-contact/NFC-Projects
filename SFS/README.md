# Secure File System (SFS)

A Django + Django REST Framework backend for encrypted file storage, with a
small template-based frontend (Bootstrap + Axios) served by Django. Users
register, log in with JWT, and upload files that are encrypted at rest;
each operation is recorded in an activity log. The repository also contains
an experimental React/Vite client prototype at the root (`App.tsx`,
`services/`), which is separate from the Django app.

## Features

- User registration and JWT authentication (djangorestframework-simplejwt)
- AES-256 file encryption, RSA-2048 per-user key pairs, HMAC-SHA256 integrity checks
- Upload, download, and delete endpoints (`/api/files/`)
- Local storage implemented; Firebase and S3 hooks included but not wired up
- Activity logging of file and auth operations

## Setup

Requires Python 3. From the repository root:

```bash
python -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
```

Configuration is read from environment variables (optionally via a `.env`
file next to `manage.py`): `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`,
`DJANGO_ALLOWED_HOSTS`, and `POSTGRES_*` for PostgreSQL. Defaults use
SQLite with debug on, so no configuration is needed for development.

```bash
cd backend/backend/sfs_backend
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open:

- API root: http://127.0.0.1:8000/api/
- Frontend: http://127.0.0.1:8000/login.html
- Admin: http://127.0.0.1:8000/admin/

## Tests

```bash
cd backend/backend/sfs_backend
python manage.py test
```

## Production notes

- Set `DJANGO_DEBUG=False` and the `POSTGRES_*` variables for PostgreSQL
- Use a strong `DJANGO_SECRET_KEY` and protect the file master key
- Restrict CORS origins and serve static files with WhiteNoise or a CDN

## Credits

Information Security course project, 3rd semester, under the supervision of
Sir Khalid Mehmood. Team: Moavia Amir, Mirza Muhammad Dawood, Arslan Nasir,
Ali Raza. Coding Moves, Engineering Branch, 2025.
