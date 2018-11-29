from django.db import models
from django.utils.translation import pgettext_lazy

from ...shipping import models as ship

import uuid

ACTIVE = 'A'
PENDING = 'P'
SUSPENDED = 'S'
CLOSED = 'C'
MERCHANT_ACCOUNT_STATUS = ((PENDING, "Pending"), (ACTIVE, "Active"), (SUSPENDED, "Suspended"), (CLOSED, "Closed"))


class Merchant(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_on = models.DateTimeField(auto_now=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    shipping_method = models.ManyToManyField(ship.ShippingMethod, related_name='merchants')
    shipping_zone = models.ManyToManyField(ship.ShippingZone, related_name="merchants")
    status = models.CharField(max_length=5, choices=MERCHANT_ACCOUNT_STATUS)
    company_name = models.CharField(max_length=30)
    company_desc = models.CharField(max_length=200)
    company_web_link = models.URLField(verbose_name="company website")
    company_image = models.ImageField(verbose_name="company image")
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=12)

    def is_active(self):
        return self.status == ACTIVE

    class Meta:
        ordering = ('-modified_on',)

    def get_all_members(self):
        return self.users.all()
