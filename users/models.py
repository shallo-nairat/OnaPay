from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)  # This is to ensure the email is unique among all our users
    user_name = models.CharField(max_length=150, unique=True)  # This is to ensure each username is unique
    password = models.CharField(max_length=255)  # This is to store password securely
    phone_number = models.CharField(max_length=20)  # Thi is to store the user's phone number
    first_name = models.CharField(max_length=255)  # This is for the users first name
    last_name = models.CharField(max_length=255)  # This is for the user's last name
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on user creation
    user_role = models.CharField(max_length=50)  # To differentiate user roles e.g., 'admin', 'client'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_name})"
