# accounts/serializers.py
from rest_framework import serializers
from .models import User, Member, SavingsAccount
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'role')
        read_only_fields = ('id',)

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'phone_number', 'role')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Member
        fields = '__all__'
        read_only_fields = ('id', 'total_shares', 'total_savings')

class SavingsAccountSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    
    class Meta:
        model = SavingsAccount
        fields = '__all__'
        read_only_fields = ('id', 'balance', 'last_transaction_date')