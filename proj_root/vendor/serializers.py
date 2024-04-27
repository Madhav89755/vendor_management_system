""" Serializer class for the Models """
from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorModelSerializer(serializers.ModelSerializer):
    """ Vendor Model Serializer """
    class Meta:
        """ Meta class """
        model=Vendor
        fields='__all__'
        read_only_fields=['id', 'created_on', 'updated_on']

class PurchaseOrderModelSerializer(serializers.ModelSerializer):
    """ PurchaseOrder Model Serializer """
    class Meta:
        """ Meta class """
        model=PurchaseOrder
        fields='__all__'
        read_only_fields=['po_number', 'created_on', 'updated_on']

class HistoricalPerformanceModelSerializer(serializers.ModelSerializer):
    """ PurchaseOrder Model Serializer """
    class Meta:
        """ Meta class """
        model=HistoricalPerformance
        fields='__all__'
        read_only_fields=['id', 'created_on', 'updated_on']
