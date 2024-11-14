# investments/models.py
from django.db import models

class Investment(models.Model):
    INVESTMENT_STATUS = (
        ('ACTIVE', 'Active'),
        ('MATURED', 'Matured'),
        ('TERMINATED', 'Terminated'),
    )
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount_invested = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateField()
    maturity_date = models.DateField()
    expected_return_rate = models.DecimalField(max_digits=5, decimal_places=2)
    actual_return = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=INVESTMENT_STATUS, default='ACTIVE')
    documents = models.FileField(upload_to='investment_documents/', null=True, blank=True)

    def __str__(self):
        return self.name