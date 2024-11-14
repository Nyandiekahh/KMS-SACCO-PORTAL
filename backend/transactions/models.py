# transactions/models.py
from django.db import models
from accounts.models import Member, User
from loans.models import Loan

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWAL', 'Withdrawal'),
        ('LOAN_DISBURSEMENT', 'Loan Disbursement'),
        ('LOAN_REPAYMENT', 'Loan Repayment'),
        ('SHARE_PURCHASE', 'Share Purchase'),
        ('DIVIDEND', 'Dividend'),
        ('FINE', 'Fine'),
    )
    
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    reference_number = models.CharField(max_length=50, unique=True)
    processed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    loan = models.ForeignKey(Loan, on_delete=models.SET_NULL, null=True, blank=True)
    balance_after = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.reference_number} - {self.member.member_number}"