import os

# Define the main project directory
main_project_dir = "student_performance_review"
os.makedirs(main_project_dir)

# Define subdirectories and their contents
subdirectories = [
    "student_performance_review",
    "apps",
    "media",
    "static",
    "templates",
]

# Create the main project directory and subdirectories
for subdirectory in subdirectories:
    os.makedirs(os.path.join(main_project_dir, subdirectory))

# Define files within subdirectories
files = {
    "student_performance_review/": ["__init__.py", "settings.py", "urls.py", "wsgi.py"],
    "apps/": ["__init__.py"],
    "apps/authentication/": ["__init__.py"],
    "apps/core/": ["__init__.py"],
    "apps/assignments/": ["__init__.py"],
    "apps/courses/": ["__init__.py"],
    "apps/communication/": ["__init__.py"],
    "media/": [],
    "static/": [],
    "templates/": [],
}

# Create files within subdirectories
for directory, file_list in files.items():
    for file_name in file_list:
        with open(os.path.join(main_project_dir, directory, file_name), "w") as file:
            pass  # Create an empty file

# Create the main project files
project_files = ["manage.py", "requirements.txt", ".gitignore", "README.md"]
for file_name in project_files:
    with open(os.path.join(main_project_dir, file_name), "w") as file:
        pass  # Create an empty file
