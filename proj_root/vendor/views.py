""" API's for the models """
from rest_framework.viewsets import ModelViewSet
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import (VendorModelSerializer,
                          PurchaseOrderModelSerializer,
                          HistoricalPerformanceModelSerializer)
# Create your views here.

class VendorViewSet(ModelViewSet):
    """ Vendor Api's """
    queryset=Vendor.objects.all()
    serializer_class=VendorModelSerializer

class PurchaseOrderViewSet(ModelViewSet):
    """ Purchase Order Api's """
    queryset=PurchaseOrder.objects.all()
    serializer_class=PurchaseOrderModelSerializer

class HistoricalPerformanceViewSet(ModelViewSet):
    """ HistoricalPerformance Api's """
    queryset=HistoricalPerformance.objects.all()
    serializer_class=HistoricalPerformanceModelSerializer
