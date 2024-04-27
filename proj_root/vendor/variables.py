"""
This file consist of all the variables 
that are commonly being used
"""
from django.utils.translation import gettext_lazy as _

PENDING = 'pending'
COMPLETED = 'completed'
CANCELLED = 'cancelled'

STATUS_CHOICES = (
    (PENDING, _(PENDING.title())),
    (COMPLETED, _(COMPLETED.title())),
    (CANCELLED, _(CANCELLED.title())),
)
