from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from .models import Account
from decimal import Decimal

class AccountModelTest(TestCase):
    def setUp(self):
        """Create a user and an account instance for testing"""
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        
        # Create an Account instance
        self.account = Account.objects.create(
            user=self.user,
            bank_name="Test Bank",
            account_number="1234567890",
            account_type="checking",
            balance=Decimal('1000.00')
        )
    
    def test_account_creation(self):
        """Test if account is created successfully"""
        self.assertEqual(self.account.bank_name, "Test Bank")
        self.assertEqual(self.account.account_number, "1234567890")
        self.assertEqual(self.account.account_type, "checking")
        self.assertEqual(self.account.balance, Decimal('1000.00'))
        self.assertEqual(self.account.user.username, "testuser")
    
    def test_account_str_method(self):
        """Test if the string representation of the account is correct"""
        expected_str = "Test Bank - checking - 1234567890"
        self.assertEqual(str(self.account), expected_str)

    def test_unique_account_number(self):
        """Test that account number is unique"""
        with self.assertRaises(Exception):  # Expect an IntegrityError when trying to create a duplicate account number
            Account.objects.create(
                user=self.user,
                bank_name="Another Bank",
                account_number="1234567890",  # Duplicate account number
                account_type="business",
                balance=Decimal('500.00')
            )
    
    def test_account_balance(self):
        """Test if balance is correctly set and handled as a Decimal"""
        self.assertIsInstance(self.account.balance, Decimal)
        self.assertEqual(self.account.balance, Decimal('1000.00'))
    
    def test_account_type_choices(self):
        """Test if the account_type field is limited to the correct choices"""
        valid_account = Account.objects.create(
            user=self.user,
            bank_name="Sample Bank",
            account_number="9876543210",
            account_type="savings",  # valid type
            balance=Decimal('2000.00')
        )
        self.assertEqual(valid_account.account_type, "savings")

        # Try invalid account type
        with self.assertRaises(ValueError):  # Expect ValueError when trying to create an invalid account type
            Account.objects.create(
                user=self.user,
                bank_name="Invalid Bank",
                account_number="1122334455",
                account_type="invalid_type",  # Invalid type
                balance=Decimal('2000.00')
            )

