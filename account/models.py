from django.db import models

# Create your models here.

# from django.contrib.auth.models import User  # Uncomment if you're using the default User model or a custom user model

class Account(models.Model):
    # Optionally link to a User (you can leave this out for now)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts", null=True, blank=True)
    
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20, unique=True)  # Ensure uniqueness
    ACCOUNT_TYPES = [  # Restrict account types to valid options
        ('savings', 'Savings'),
        ('checking', 'Checking'),
        ('business', 'Business'),
    ]
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bank_name} - {self.account_type} - {self.account_number}"
