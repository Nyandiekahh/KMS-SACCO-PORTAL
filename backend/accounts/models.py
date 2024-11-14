# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from decimal import Decimal

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrator'),
        ('MEMBER', 'Member'),
        ('STAFF', 'Staff'),
    )
    
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='MEMBER')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

class Member(models.Model):
    MEMBERSHIP_STATUS = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('SUSPENDED', 'Suspended'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_number = models.CharField(max_length=20, unique=True)
    id_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=100)
    address = models.TextField()
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_phone = models.CharField(max_length=15)
    next_of_kin_relation = models.CharField(max_length=50)
    membership_status = models.CharField(max_length=10, choices=MEMBERSHIP_STATUS, default='ACTIVE')
    total_shares = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_savings = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member_number} - {self.user.get_full_name()}"

class SavingsAccount(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    minimum_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    last_transaction_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.account_number} - {self.member.member_number}"