""" Admin classes for the admin panel """
from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance
# Register your models here.

@admin.register(Vendor)
class VendorModelAdmin(admin.ModelAdmin):
    """ Admin Class for Vendor Model """
    list_display=["id", "vendor_code",
                  "name", "contact_details",
                  "created_on"]
    search_fields=["id", "vendor_code",
                  "name"]
    readonly_fields = ['created_on', 'updated_on']

@admin.register(PurchaseOrder)
class PurchaseOrderModelAdmin(admin.ModelAdmin):
    """ Admin Class for PurchaseOrder Model """
    list_display=["po_number", "vendor",
                  "order_date", "delivery_date",
                  "created_on"]
    search_fields=["po_number", "vendor"]
    list_filter=["status"]
    readonly_fields = ['created_on', 'updated_on']

@admin.register(HistoricalPerformance)
class HistoricalPerformanceModelAdmin(admin.ModelAdmin):
    """ Admin Class for HistoricalPerformance Model """
    list_display=["id", "vendor",
                  "date", "on_time_delivery_rate",
                  "created_on"]
    search_fields=["id", "vendor"]
    readonly_fields = ['created_on', 'updated_on']
