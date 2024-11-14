# transactions/serializers.py
from rest_framework import serializers
from .models import Transaction
from accounts.serializers import MemberSerializer, UserSerializer
from loans.serializers import LoanSerializer

class TransactionSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    processed_by = UserSerializer(read_only=True)
    loan = LoanSerializer(read_only=True)
    
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('id', 'date', 'reference_number', 'processed_by', 'balance_after')

class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('member', 'transaction_type', 'amount', 'description', 'loan')

    def create(self, validated_data):
        # Generate reference number
        import uuid
        validated_data['reference_number'] = f"TRX-{uuid.uuid4().hex[:8].upper()}"
        
        # Set the processed_by field to the current user
        user = self.context['request'].user
        validated_data['processed_by'] = user
        
        return super().create(validated_data)