from django.test import TestCase

# Create your tests here.
from account.models import Account
from .models import Statement
from decimal import Decimal


class StatementModelTest(TestCase):
    def setUp(self):
        # This isto setup an Account instance to link to Statement
        self.account = Account.objects.create(
            bank_name="Test Bank",
            account_number="1234567890",
            account_type="savings",
            balance=Decimal('1000.00'),
        )
        
    def test_create_statement(self):
        # Create a Statement instance
        statement = Statement.objects.create(
            account=self.account,
            description="Account Transfer",
            amount=Decimal('200.00'),
            transaction_type="debit",
        )
        
        # Assert that the Statement object was created and linked to the Account
        self.assertEqual(statement.account, self.account)  # Check if the statement is linked to the correct account
        self.assertEqual(statement.description, "Account Transfer")  # Check the description field
        self.assertEqual(statement.amount, Decimal('200.00'))  # Check if the amount is correctly set
        self.assertEqual(statement.transaction_type, "debit")  # Check the transaction type field
        self.assertEqual(str(statement), "Test Bank - Account Transfer - 200.00")  # Test the __str__ method
        
    def test_statement_default_date(self):
        # This is a statement instance without specifying the date 
        statement = Statement.objects.create(
            account=self.account,
            description="Transfer",
            amount=Decimal('500.00'),
            transaction_type="credit",
        )
        
        # Assert that the date is today (or the default date set by auto_now_add)
        self.assertEqual(statement.date, statement.date.today())  # Check if the date is today's date
