# loans/serializers.py
from rest_framework import serializers
from .models import LoanType, Loan
from accounts.serializers import MemberSerializer, UserSerializer

class LoanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanType
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    loan_type = LoanTypeSerializer(read_only=True)
    approved_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Loan
        fields = '__all__'
        read_only_fields = ('id', 'status', 'approved_by', 'total_payable', 'balance',
                           'disbursement_date', 'completion_date')

class LoanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('member', 'loan_type', 'amount_requested', 'term', 'purpose')

    def create(self, validated_data):
        loan_type = validated_data['loan_type']
        validated_data['interest_rate'] = loan_type.interest_rate
        return super().create(validated_data)