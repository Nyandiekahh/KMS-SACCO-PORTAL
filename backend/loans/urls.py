# loans/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'loans', views.LoanViewSet, basename='loan')
router.register(r'loan-types', views.LoanTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
