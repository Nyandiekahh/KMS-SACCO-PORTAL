from rest_framework import serializers
from .models import User, Member

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'role', 'phone_number', 'date_joined', 'is_active')
        read_only_fields = ('id', 'date_joined')

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Member
        fields = (
            'id',
            'user',
            'member_number',
            'id_number',
            'date_of_birth',
            'occupation',
            'address',
            'next_of_kin_name',
            'next_of_kin_phone',
            'next_of_kin_relation',
            'membership_status',
            'total_shares',
            'share_percentage',
            'total_debt',
            'joining_date'
        )
        read_only_fields = ('id', 'member_number', 'joining_date')