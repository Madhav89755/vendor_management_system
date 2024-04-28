""" Routes for the api's """
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (VendorViewSet, PurchaseOrderViewSet,
                    HistoricalPerformanceViewSet)
router = DefaultRouter()

router.register(r'vendor', VendorViewSet, basename="vendor")
router.register(r'purchase-order', PurchaseOrderViewSet,
                basename="purchase-order")
router.register(r'historical-performance',
                HistoricalPerformanceViewSet, basename="performance")

urlpatterns = [
    path("", include(router.urls))
]
