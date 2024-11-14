from rest_framework import serializers
from .models import Loan, LoanType
from accounts.models import Member
from accounts.serializers import MemberSerializer

class LoanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanType
        fields = (
            'id',
            'name',
            'description',
            'interest_rate',
            'term_period',
            'min_amount',
            'max_amount',
            'requirements',
            'is_active'
        )

class LoanSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    loan_type = LoanTypeSerializer(read_only=True)
    loan_type_id = serializers.IntegerField(write_only=True)
    member_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Loan
        fields = (
            'id',
            'member',
            'member_id',
            'loan_type',
            'loan_type_id',
            'amount',
            'interest_amount',
            'total_amount',
            'term_period',
            'monthly_payment',
            'disbursement_date',
            'due_date',
            'purpose',
            'status',
            'application_date',
            'approval_date',
            'approved_by',
            'disbursed_by',
            'notes'
        )
        read_only_fields = (
            'id',
            'interest_amount',
            'total_amount',
            'monthly_payment',
            'due_date',
            'application_date',
            'approval_date',
            'approved_by',
            'disbursed_by'
        )

    def create(self, validated_data):
        # Extract member_id and loan_type_id
        member_id = validated_data.pop('member_id')
        loan_type_id = validated_data.pop('loan_type_id')
        
        # Get the actual Member and LoanType instances
        member = Member.objects.get(id=member_id)
        loan_type = LoanType.objects.get(id=loan_type_id)
        
        # Create the loan
        loan = Loan.objects.create(
            member=member,
            loan_type=loan_type,
            **validated_data
        )
        
        return loan

    def validate(self, data):
        """
        Check that the loan amount is within the allowed range for the loan type
        """
        loan_type = LoanType.objects.get(id=data['loan_type_id'])
        amount = data['amount']
        
        if amount < loan_type.min_amount:
            raise serializers.ValidationError(
                f"Loan amount must be at least {loan_type.min_amount}"
            )
        if amount > loan_type.max_amount:
            raise serializers.ValidationError(
                f"Loan amount cannot exceed {loan_type.max_amount}"
            )
            
        return data