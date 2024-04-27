""" Model File for the project """
from django.db.models import (Model, DateTimeField,
                              CharField, TextField,
                              FloatField, IntegerField,
                              ForeignKey, JSONField,
                              CASCADE)
from django.utils.translation import gettext_lazy as _
from .variables import STATUS_CHOICES, PENDING
# Create your models here.


class DateTimeCommonFields(Model):
    """ Abstract model for date time common fields """

    created_on = DateTimeField(_("Created On"), auto_now_add=True)
    updated_on = DateTimeField(_("Updated On"), auto_now=True)

    class Meta:
        """ Meta Class """
        abstract = True


class Vendor(DateTimeCommonFields):
    """ Vendor Model """

    name = CharField(_("Vendor Name"),
                     max_length=255,
                     help_text=_("Vendor's name"))
    contact_details = TextField(_("Contact Detail"),
                                help_text=_("Contact information of the vendor"))
    address = TextField(_("Address"),
                        help_text=_("Physical address of the vendor"))
    vendor_code = CharField(_("Vendor Code"),
                            max_length=50,
                            unique=True,
                            help_text=_("A unique identifier for the vendor."))
    on_time_delivery_rate = FloatField(_("On time delivery rate"),
                                       default=0,
                                       help_text=_("Tracks the percentage \
                                                   of on-time deliveries"))
    quality_rating_avg = FloatField(_("Quality Rating Average"),
                                    default=0,
                                    help_text=_("Average rating of quality \
                                                based on purchase orders"))
    average_response_time = FloatField(_("Average Response Time"),
                                       default=0,
                                       help_text=_("Average time taken to \
                                                   acknowledge purchase orders"))
    fulfillment_rate = FloatField(_("Fulfillment Rate"),
                                  default=0,
                                  help_text=_("Percentage of purchase \
                                              orders fulfilled successfully"))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        """ Meta class """
        verbose_name = _("Vendor")
        verbose_name_plural = _("Vendors")
        ordering = ['-created_on']


def purchase_order_number():
    """ function to generate purchase order number """
    objs=PurchaseOrder.objects.all()
    if objs.count()==0:
        count=1
    else:
        count=int(objs.first().po_number)+1
    count=str(count).zfill(3)
    return count


class PurchaseOrder(DateTimeCommonFields):
    """ Purchase Order Model """

    po_number = CharField(_("Purchase Order"),
                          max_length=50,
                          primary_key=True,
                          editable=False,
                          default=purchase_order_number,
                          help_text=_("Unique number identifying the PO"))
    vendor = ForeignKey(verbose_name=_("Vendor"),
                        to=Vendor, on_delete=CASCADE,
                        help_text=_("Link to the Vendor"))
    order_date = DateTimeField(_("Order Date"),
                               help_text=_("Date when the order was placed"))
    delivery_date = DateTimeField(_("Delivery Date"),
                                  help_text=_("Expected or actual delivery \
                                              date of the order"))
    items = JSONField(_("Items"),
                      help_text=_("Details of items ordered"))
    quantity = IntegerField(_("Quantity"),
                            default=0,
                            help_text=_("Total quantity of items \
                                        in the PO"))
    status = CharField(_("Status"),
                       max_length=20,
                       choices=STATUS_CHOICES,
                       default=PENDING,
                       help_text=_("Current status of the PO"))
    quality_rating = FloatField(_("Quality Rating"),
                                null=True,
                                blank=True,
                                help_text=_("Rating given to the vendor for \
                                            this PO"))
    issue_date = DateTimeField(_("Issue Date"),
                               auto_now_add=True,
                               help_text=_("Timestamp when the PO was issued \
                                           to the vendor"))
    acknowledgment_date = DateTimeField(_("Acknowledgement Date"),
                                        null=True,
                                        blank=True,
                                        help_text=_("Timestamp when the vendor \
                                                    acknowledged the PO"))

    def __str__(self):
        return f"{self.po_number}"

    class Meta:
        """ Meta class """
        verbose_name = _("Purchase Order")
        verbose_name_plural = _("Purchase Orders")
        ordering = ['-created_on']


class HistoricalPerformance(DateTimeCommonFields):
    """ Historical Performance Model """

    vendor = ForeignKey(verbose_name=_("Vendor"),
                        to=Vendor,
                        on_delete=CASCADE,
                        help_text=_("Link to the Vendor"))
    date = DateTimeField(help_text=_("Date of the performance record"))
    on_time_delivery_rate = FloatField(_("On Time Delivery Rate"),
                                       default=0,
                                       help_text=_("Historical record of the \
                                                   on-time delivery rate"))
    quality_rating_avg = FloatField(_("Quality Rating Average"),
                                    default=0,
                                    help_text=_("Historical record of the \
                                                quality rating average"))
    average_response_time = FloatField(_("Average Response Time"),
                                       default=0,
                                       help_text=_("Historical record of the \
                                                   average response time"))
    fulfillment_rate = FloatField(_("Fulfillment Rate"),
                                  default=0,
                                  help_text=_("Historical record of the \
                                              fulfilment rate."))

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"

    class Meta:
        """ Meta class """
        verbose_name = _("Historical Performance")
        verbose_name_plural = _("Historical Performances")
        ordering = ['-created_on']
