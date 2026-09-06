# Job Portal

A full-stack job portal built with Django, connecting job-seeking candidates with hiring companies through a single platform.

## Features
- **Role-based authentication** — separate signup/profile flows for candidates and companies, built on a custom Django user model
- **Company & candidate profiles** — resumes, portfolios, and company details with image/file uploads
- **Job management** — full CRUD for job postings, restricted to the owning company
- **Search & filtering** — search by keyword, filter by job type, experience level, and location
- **Application system** — candidates apply with an optional cover message; companies review and update application status (Pending → Reviewed → Accepted/Rejected)
- **Dashboards** — "My Jobs" for companies, "My Applications" for candidates
- **Pagination & query optimization** — all list views paginated, N+1 queries resolved with `select_related`

## Tech Stack
Python · Django · PostgreSQL/SQLite · Tailwind CSS · Django Templates

## Getting Started
1. Clone the repo and create a virtual environment
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in `SECRET_KEY`, `DEBUG`, etc.
4. `python manage.py migrate`
5. `python manage.py runserver`