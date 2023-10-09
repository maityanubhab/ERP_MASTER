# ERP_MASTER

student_performance_review/
│
├── student_performance_review/   # Main Django project directory
│   ├── __init__.py               # An empty file indicating a Python package
│   ├── settings.py               # Django project settings
│   ├── urls.py                   # URL routing for the project
│   ├── wsgi.py                   # WSGI configuration for deployment
│
├── apps/                        # Custom Django apps for project functionality
│   ├── __init__.py               # An empty file indicating a Python package
│   ├── authentication/           # App for user authentication
│   ├── core/                     # App for core functionality (e.g., models)
│   ├── assignments/              # App for assignment-related features
│   ├── courses/                  # App for course-related features
│   ├── communication/            # App for messaging and meetings
│   ├── static/                   # Static files (CSS, JavaScript, etc.)
│   ├── templates/                # HTML templates
│   ├── migrations/               # Database migrations
│   └── ...                       # Additional custom apps
│
├── media/                        # User-uploaded media files (e.g., assignment submissions)
│
├── static/                       # Project-wide static files (e.g., base CSS)
│
├── templates/                    # Project-wide templates (e.g., base HTML)
│
├── manage.py                     # Django's command-line utility for project management
│
├── requirements.txt              # List of project dependencies
│
├── .gitignore                    # Configuration file specifying files and directories to ignore by version control
│
├── README.md                     # Project documentation
