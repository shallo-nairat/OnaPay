from rest_framework import serializers
from account.models import Account
from statement.models import Statement
from budget.models import Budget



# pylint: disable=no-member

class AccountSerializer(serializers.ModelSerializer):
    """AccountSerializer: Serializes the Account model for API interactions.
    Converts Account objects to and from JSON """

    class Meta:
        model = Account
        fields = [
            'bank_name', 'account_number', 'account_type', 'balance', 'created_at'
        ]


class MinimalAccountSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    account_type_display = serializers.SerializerMethodField()  # To display account type name (e.g., "Savings")

    def get_account_type_display(self, obj):
        return obj.get_account_type_display()

    class Meta:
        model = Account
        fields = [
            'id', 'user_id', 'bank_name', 'account_number', 'account_type_display', 'balance'
        ]

class StatementSerializer(serializers.ModelSerializer):
    account = AccountSerializer()  # This will nest the Account details within the Statement

    class Meta:
        model = Statement
        fields = ['id', 'account', 'date', 'description', 'amount', 'transaction_type']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'category', 'amount', 'month', 'year']
