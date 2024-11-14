# kms_sacco/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # We'll uncomment these later
    # path('api/accounts/', include('accounts.urls')),
    # path('api/loans/', include('loans.urls')),
    # path('api/transactions/', include('transactions.urls')),
    # path('api/investments/', include('investments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)