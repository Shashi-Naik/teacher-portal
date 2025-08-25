from django.core.management.base import BaseCommand
from myapp.models import Teacher
from myapp.helpers import hash_password

class Command(BaseCommand):
    help = "Create a New Teacher User"
    
    def handle(self, *args, **kwargs):
        user_name = input("Enter User Name: ")
        password = input("Enter Password:  ")
        hashed_password, salt = hash_password(password)
        Teacher.objects.create(username = user_name,password_hash = hashed_password, salt=salt)
        self.stdout.write(self.style.SUCCESS(f"User [teacher] {user_name} created successfully" ))
        
        