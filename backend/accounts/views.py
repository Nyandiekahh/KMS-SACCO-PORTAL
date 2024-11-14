from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from django.db import models
from .models import User, Member
from .serializers import UserSerializer, MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'ADMIN':
            return Member.objects.all()
        return Member.objects.filter(user=self.request.user)

class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'ADMIN':
            try:
                member = Member.objects.get(user=request.user)
                return Response({
                    'total_shares': member.total_shares,
                    'share_percentage': member.share_percentage,
                    'total_debt': member.total_debt
                })
            except Member.DoesNotExist:
                return Response({
                    'error': 'Member profile not found'
                }, status=status.HTTP_404_NOT_FOUND)
        
        # Admin stats
        total_shares = Member.objects.aggregate(total=models.Sum('total_shares'))['total'] or 0
        total_debt = Member.objects.aggregate(total=models.Sum('total_debt'))['total'] or 0
        member_count = Member.objects.count()
        
        return Response({
            'total_shares': total_shares,
            'total_debt': total_debt,
            'member_count': member_count
        })