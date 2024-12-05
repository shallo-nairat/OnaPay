
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from account.models import Account  # Import the Account model
from api.serializer import AccountSerializer  # Import the serializer for Account
from statement.models import Statement
from .serializer import StatementSerializer

class AccountListView(APIView):
    """API View for getting a list of accounts and creating new accounts"""
    
    def get(self, request):
        """Retrieve all accounts"""
        accounts = Account.objects.all()  # Get all accounts from the database
        serializer = AccountSerializer(accounts, many=True)  # Serialize the list of accounts
        return Response(serializer.data)  # Return the serialized data
    
    def post(self, request):
        """Create a new account"""
        serializer = AccountSerializer(data=request.data)  # Initialize the serializer with the incoming data
        
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the new account to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created account data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if data is invalid


class AccountDetailView(APIView):
    """API View for handling details of a specific account (GET, PATCH, DELETE)"""
    
    def get(self, request, id):
        """Retrieve a specific account by ID"""
        try:
            account = Account.objects.get(id=id)  # Try to get the account by ID
        except Account.DoesNotExist:
            return Response({"detail": "Account not found"}, status=status.HTTP_404_NOT_FOUND)  # Return 404 if not found

        serializer = AccountSerializer(account)  # Serialize the account data
        return Response(serializer.data)  # Return the serialized account data
    
    def patch(self, request, id):
        """Update a specific account by ID"""
        try:
            account = Account.objects.get(id=id)  # Try to get the account by ID
        except Account.DoesNotExist:
            return Response({"detail": "Account not found"}, status=status.HTTP_404_NOT_FOUND)  # Return 404 if not found

        serializer = AccountSerializer(account, data=request.data, partial=True)  # Allow partial updates
        if serializer.is_valid():
            serializer.save()  # Save the updated account data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return the updated account data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors if any

    def delete(self, request, id):
        """Delete a specific account by ID"""
        try:
            account = Account.objects.get(id=id)  # Try to get the account by ID
        except Account.DoesNotExist:
            return Response({"detail": "Account not found"}, status=status.HTTP_404_NOT_FOUND)  # Return 404 if not found

        account.delete()  # Delete the account from the database
        return Response({"detail": "Account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)  # Return success message


class StatementListView(APIView):
    def get(self, request, account_id):
        statements = Statement.objects.filter(account_id=account_id)
        serializer = StatementSerializer(statements, many=True)
        return Response(serializer.data)

class StatementDetailView(APIView):
    def get(self, request, pk):
        try:
            statement = Statement.objects.get(pk=pk)
        except Statement.DoesNotExist:
            return Response({"detail": "Statement not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = StatementSerializer(statement)
        return Response(serializer.data)