Teacher Portal

Django-based Teacher Portal with custom login/session management and student CRUD operations.
This project demonstrates secure authentication, clean architecture, and a simple modal-based UI for managing students.


Setup Instructions
1. Clone the repository
git clone https://github.com/Shashi-Naik/teacher-portal.git
cd teacher-portal

2. Create and activate virtual environment
# Install virtualenv if not installed
pip install virtualenv

# Create virtual environment (you can give any name instead of env)
virtualenv env  

# Activate environment
env\Scripts\activate      # On Windows
source env/bin/activate   # On Mac/Linux

3. Install dependencies
pip install django

4. Database setup
python manage.py makemigrations
python manage.py migrate

5. Create a Teacher (login user)
python manage.py create_teacher


6. Run the development server
python manage.py runserver


7. Access the application
http://127.0.0.1:8000

















