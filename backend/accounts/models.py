# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrator'),
        ('MEMBER', 'Member'),
        ('STAFF', 'Staff'),
    )
    
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='MEMBER')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Member(models.Model):
    MEMBERSHIP_STATUS = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('SUSPENDED', 'Suspended'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_number = models.CharField(max_length=20, unique=True, blank=True)
    id_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    next_of_kin_name = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin_phone = models.CharField(max_length=15, null=True, blank=True)
    next_of_kin_relation = models.CharField(max_length=50, null=True, blank=True)
    membership_status = models.CharField(max_length=10, choices=MEMBERSHIP_STATUS, default='ACTIVE')
    total_shares = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    share_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_debt = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    joining_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.member_number:
            # Generate random member number if not provided
            while True:
                random_number = ''.join(random.choices(string.digits, k=3))
                member_number = f"KMS{random_number}"
                if not Member.objects.filter(member_number=member_number).exists():
                    self.member_number = member_number
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.member_number} - {self.user.get_full_name()}"