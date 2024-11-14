# investments/serializers.py
from rest_framework import serializers
from .models import Investment

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'
        read_only_fields = ('id', 'status', 'actual_return')

class InvestmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ('name', 'description', 'amount_invested', 'start_date', 
                 'maturity_date', 'expected_return_rate', 'documents')