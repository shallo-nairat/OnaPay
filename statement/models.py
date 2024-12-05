from django.db import models

from account.models import Account
# pylint: disable=no-member


class Statement(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="statements")
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10,
        choices=[("credit", "Credit"), ("debit", "Debit")]
    )

    def __str__(self):
        return f"{self.account.bank_name} - {self.description} - {self.amount}"
