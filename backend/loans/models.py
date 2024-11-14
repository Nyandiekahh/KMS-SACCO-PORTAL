# loans/models.py
from django.db import models
from accounts.models import Member, User

class LoanType(models.Model):
    LOAN_CATEGORIES = (
        ('MEMBER', 'Member Loan'),
        ('NON_MEMBER', 'Non-Member Loan'),
    )
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=LOAN_CATEGORIES)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Loan(models.Model):
    LOAN_STATUS = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('DEFAULTED', 'Defaulted'),
    )

    member = models.ForeignKey(Member, related_name='member_loans', on_delete=models.CASCADE)
    loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term = models.IntegerField()  # in months
    status = models.CharField(max_length=20, choices=LOAN_STATUS, default='PENDING')
    application_date = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.member.member_number} - {self.loan_type.name} - {self.amount}"