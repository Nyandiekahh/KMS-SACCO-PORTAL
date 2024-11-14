# loans/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Loan, LoanType
from .serializers import LoanSerializer, LoanTypeSerializer

class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'ADMIN':
            return Loan.objects.all()
        return Loan.objects.filter(member__user=self.request.user)

class LoanTypeViewSet(viewsets.ModelViewSet):
    queryset = LoanType.objects.all()
    serializer_class = LoanTypeSerializer
    permission_classes = [IsAuthenticated]