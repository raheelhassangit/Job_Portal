# Job Portal

A full-stack **job recruitment platform built with Django**, connecting job-seeking candidates with companies through a role-based web application.

## Features

* **Role-Based Authentication** — Separate authentication and profile workflows for candidates and companies using a custom Django user model.
* **Candidate & Company Profiles** — Manage resumes, portfolios, company information, profile images, and other professional details.
* **Job Management** — Companies can create, update, view, and delete their own job postings.
* **Job Search & Filtering** — Search jobs by keywords and filter by job type, experience level, and location.
* **Application System** — Candidates can apply for jobs with an optional cover message.
* **Application Management** — Companies can review applications and update their status: `Pending → Reviewed → Accepted / Rejected`.
* **Candidate Dashboard** — Candidates can view and manage their submitted applications.
* **Company Dashboard** — Companies can manage their job postings and review applicants.
* **Pagination** — Job and application listings are paginated for better usability and performance.
* **Query Optimization** — Uses Django ORM optimization such as `select_related` to reduce unnecessary database queries.
* **Responsive UI** — Built with Tailwind CSS and Django Templates.

## Tech Stack

| Technology          | Purpose               |
| ------------------- | --------------------- |
| Python              | Backend programming   |
| Django              | Web framework         |
| PostgreSQL / SQLite | Database              |
| Django ORM          | Database interaction  |
| Tailwind CSS        | Frontend styling      |
| Django Templates    | Server-side rendering |
| HTML                | Page structure        |
| Git & GitHub        | Version control       |

## Screenshots

### Home · Job Listings · Job Detail

| Home             | Job Listings     | Job Detail       |
| ---------------- | ---------------- | ---------------- |
| *Add screenshot* | *Add screenshot* | *Add screenshot* |

### Profiles · Applicants

| Candidate Profile | Company Profile  | Applicants       |
| ----------------- | ---------------- | ---------------- |
| *Add screenshot*  | *Add screenshot* | *Add screenshot* |

## Project Structure

```text
Job_Portal/
│
├── accounts/          # Custom user model and authentication
├── profiles/          # Candidate and company profiles
├── jobs/              # Jobs, applications, search and filtering
├── theme/             # Tailwind CSS integration
├── config/            # Project settings and URL configuration
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/raheelhassangit/Job_Portal.git
cd Job_Portal
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on `.env.example` and configure the required settings such as:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

Add your database configuration if PostgreSQL is being used.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an admin account

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Core Workflow

### Candidate

```text
Register
   ↓
Create Profile
   ↓
Browse / Search Jobs
   ↓
View Job Details
   ↓
Submit Application
   ↓
Track Application Status
```

### Company

```text
Register
   ↓
Create Company Profile
   ↓
Create Job Posting
   ↓
Manage Jobs
   ↓
View Applicants
   ↓
Update Application Status
```

## Database Relationships

The application uses Django's relational ORM to connect users, profiles, jobs, and applications.

```text
User
├── Candidate Profile
│      └── Applications
│             └── Job
│
└── Company Profile
       └── Jobs
              └── Applications
```

This structure allows candidates and companies to interact while maintaining ownership and access restrictions.

## Learning Objectives

This project was built to gain practical experience with:

* Django project and app architecture
* Custom Django user models
* Authentication and authorization
* Django models and relationships
* Django ORM and query optimization
* ModelForms and validation
* CRUD operations
* File and image uploads
* Search and filtering
* Pagination
* Role-based access control
* Application workflows
* Tailwind CSS integration
* PostgreSQL database integration

## Future Improvements

* Django REST Framework API
* Token/JWT authentication
* Advanced job recommendations
* Email notifications
* Saved/bookmarked jobs
* Company verification
* Resume parsing
* AI-powered job matching
* Automated testing
* Production deployment

## License

This project was developed for **educational and portfolio purposes**.
