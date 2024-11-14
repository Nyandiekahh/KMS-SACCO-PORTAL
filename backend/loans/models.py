# loans/models.py
from django.db import models
from accounts.models import Member, User

class LoanType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    maximum_amount = models.DecimalField(max_digits=12, decimal_places=2)
    minimum_amount = models.DecimalField(max_digits=12, decimal_places=2)
    maximum_term = models.IntegerField()  # in months
    processing_fee = models.DecimalField(max_digits=5, decimal_places=2)
    requirements = models.TextField()

    def __str__(self):
        return self.name

class Loan(models.Model):
    LOAN_STATUS = (
        ('PENDING', 'Pending Approval'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('DISBURSED', 'Disbursed'),
        ('COMPLETED', 'Completed'),
        ('DEFAULTED', 'Defaulted'),
    )
    
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    amount_requested = models.DecimalField(max_digits=12, decimal_places=2)
    amount_approved = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term = models.IntegerField()  # in months
    purpose = models.TextField()
    status = models.CharField(max_length=20, choices=LOAN_STATUS, default='PENDING')
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='approved_loans')
    disbursement_date = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    total_payable = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, null=True)

    def __str__(self):
        return f"Loan-{self.id} - {self.member.member_number}"