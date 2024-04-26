""" Model File for the project """
from django.db.models import (Model,
                              DateTimeField,
                              CharField,
                              TextField,
                              FloatField,
                              IntegerField,
                              ForeignKey,
                              JSONField,
                              CASCADE)
from django.utils.translation import gettext_lazy as _

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

    name = CharField(max_length=255,
                            help_text=_("Vendor's name"))
    contact_details = TextField(
        help_text=_("Contact information of the vendor"))
    address = TextField(
        help_text=_("Physical address of the vendor"))
    vendor_code = CharField(max_length=50,
                                   unique=True,
                                   help_text=_("A unique identifier for the vendor."))
    on_time_delivery_rate = FloatField(default=0,
                                              help_text=_("Tracks the percentage \
                                                          of on-time deliveries"))
    quality_rating_avg = FloatField(default=0,
                                           help_text=_("Average rating of quality \
                                                       based on purchase orders"))
    average_response_time = FloatField(default=0,
                                              help_text=_("Average time taken to \
                                                          acknowledge purchase orders"))
    fulfillment_rate = FloatField(default=0,
                                         help_text=_("Percentage of purchase \
                                                     orders fulfilled successfully"))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        """ Meta class """
        verbose_name = _("Vendor")
        verbose_name_plural = _("Vendors")
        ordering = ['-created_on']


PENDING = 'pending'
COMPLETED = 'completed'
CANCELLED = 'cancelled'

STATUS_CHOICES = (
    (PENDING, _(PENDING.title())),
    (COMPLETED, _(COMPLETED.title())),
    (CANCELLED, _(CANCELLED.title())),
)


class PurchaseOrder(DateTimeCommonFields):
    """ Purchase Order Model """

    po_number = CharField(max_length=50, primary_key=True,
                                 help_text=_("Unique number identifying the PO"))
    vendor = ForeignKey(Vendor, on_delete=CASCADE,
                               help_text=_("Link to the Vendor"))
    order_date = DateTimeField(
        help_text=_("Date when the order was placed"))
    delivery_date = DateTimeField(help_text=_("Expected or actual delivery \
                                                     date of the order"))
    items = JSONField(help_text=_("Details of items ordered"))
    quantity = IntegerField(default=0, help_text=_("Total quantity of items \
                                                          in the PO"))
    status = CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default=PENDING,
                              help_text=_("Current status of the PO"))
    quality_rating = FloatField(null=True, blank=True,
                                       help_text=_("Rating given to the vendor for \
                                                   this PO"))
    issue_date = DateTimeField(auto_now_add=True,
                                      help_text=_("Timestamp when the PO was issued \
                                                  to the vendor"))
    acknowledgment_date = DateTimeField(null=True, blank=True,
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

    vendor = ForeignKey(Vendor, on_delete=CASCADE,
                        help_text=_("Link to the Vendor"))
    date = DateTimeField(help_text=_("Date of the performance record"))
    on_time_delivery_rate = FloatField(default=0,
                                       help_text=_("Historical record of the on-time \
                                                   delivery rate"))
    quality_rating_avg = FloatField(default=0,
                                    help_text=_("Historical record of the quality rating \
                                                average"))
    average_response_time = FloatField(default=0,
                                       help_text=_("Historical record of the average \
                                                   response time"))
    fulfillment_rate = FloatField(default=0,
                                  help_text=_("Historical record of the fulfilment rate."))

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"

    class Meta:
        """ Meta class """
        verbose_name = _("Historical Performance")
        verbose_name_plural = _("Historical Performances")
        ordering = ['-created_on']
