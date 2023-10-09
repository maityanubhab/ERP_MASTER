import os

# Define the project root directory
project_root = "student_performance_review"

# Define the app names
app_names = ["authentication", "core", "assignments", "courses", "communication"]

# Create the project root directory
os.makedirs(project_root, exist_ok=True)

# Create the project-level files
project_files = ["manage.py", "requirements.txt", ".gitignore", "README.md"]
for file in project_files:
    open(os.path.join(project_root, file), "w").close()

# Create the project-level directories
project_directories = ["media", "static", "templates"]
for directory in project_directories:
    os.makedirs(os.path.join(project_root, directory), exist_ok=True)

# Create the main app directory
os.makedirs(os.path.join(project_root, "apps"), exist_ok=True)

# Create app directories and files
for app_name in app_names:
    app_dir = os.path.join(project_root, "apps", app_name)
    os.makedirs(app_dir, exist_ok=True)

    # Create app-specific files
    app_files = ["__init__.py", "admin.py", "apps.py", "models.py", "tests.py", "views.py"]
    for file_name in app_files:
        open(os.path.join(app_dir, file_name), "w").close()

    # Create app-specific directories
    app_directories = ["migrations", "static", "templates"]
    for directory_name in app_directories:
        os.makedirs(os.path.join(app_dir, directory_name), exist_ok=True)
