# Django Academic System

A full-featured academic management web application built with Django. Manage students, courses, and course registrations through a clean, authenticated interface styled with a dark gold-and-maroon design system.

---
## Live Demo
🌐 https://django-academic-system-production.up.railway.app

## Features

- **Student Management** — Create, view, edit, and delete student records
- **Course Catalogue** — Manage courses with codes, instructors, and credit hours
- **Registration Tracking** — Enrol students into courses and track grades
- **User Authentication** — Login/logout with session-based auth; protected dashboard
- **Responsive Design** — Mobile-friendly layout with hamburger navigation
- **Custom Design System** — Dark background with gold/maroon accents, serif + geometric sans-serif typography

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Django 6.x |
| Database | SQLite3 |
| Frontend | Django Templates, vanilla CSS |
| Fonts | Space Grotesk, Cormorant Garamond (Google Fonts) |
| Auth | Django built-in authentication |

---

## Project Structure

```
core/                   # Django project settings & URLs
main/
  models.py             # Student, Course, Registration models
  views.py              # CRUD views + auth-protected dashboard
  forms.py              # ModelForms
  urls.py               # App URL routing
  templates/
    base.html           # Shared layout (navbar, fonts, CSS)
    home.html           # Landing page with feature cards
    dashboard.html      # Auth-protected dashboard
    student_list.html   # Student card grid
    course_list.html    # Course table
    registration_list.html
    student_form.html   # Add / edit form
    course_form.html
    registration_form.html
    registration/
      login.html        # Standalone login page
static/
  css/style.css         # Full design system
```

---

## Models

**Student**
- `name` — CharField
- `email` — EmailField

**Course**
- `course_code` — CharField
- `course_name` — CharField
- `instructor` — CharField
- `credits` — IntegerField

**Registration**
- `student` — ForeignKey → Student
- `course` — ForeignKey → Course
- `registration_date` — DateField (auto)
- `grade` — CharField (optional)

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Hiralama123/django-academic-system.git
cd django-academic-system

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install django

# 4. Apply database migrations
python manage.py migrate

# 5. Create a superuser (for login)
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```
---

## Usage

| URL | Description |
|---|---|
| `/` | Home page |
| `/students/` | Student list |
| `/students/add/` | Add a student |
| `/courses/` | Course catalogue |
| `/courses/add/` | Add a course |
| `/registrations/` | Registration list |
| `/registrations/add/` | Register a student |
| `/dashboard/` | Protected dashboard (login required) |
| `/login/` | Login page |
| `/admin/` | Django admin panel |

---

## License

MIT
