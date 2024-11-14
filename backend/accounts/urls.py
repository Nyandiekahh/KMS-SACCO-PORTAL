from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'members', views.MemberViewSet, basename='member')

urlpatterns = [
    path('', include(router.urls)),
    path('members/dashboard_stats/', views.DashboardStatsView.as_view(), name='dashboard-stats'),
]