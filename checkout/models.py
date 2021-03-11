import uuid

from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.db import models

from common.utils import unique_order_generator
from products.models import Product


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_number = models.CharField(max_length=8,
                                    null=True,
                                    blank=True,
                                    unique=True,
                                    editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        null=False,
                                        default=0)
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0)

    def update_total(self):
        """
        Update grand total each time a line item is added,
        adding in delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def __str__(self):
        return self.order_number


def pre_save_create_order(sender, instance, *args, **kwargs):
    if not instance.order_number:
        instance.order_number = unique_order_generator(instance)


pre_save.connect(pre_save_create_order, sender=Order)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order,
                              null=False,
                              blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False,
                                   blank=False,
                                   default=0)
    lineitem_total = models.DecimalField(max_digits=6,
                                         decimal_places=2,
                                         null=False,
                                         blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'


def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


post_save.connect(update_on_save, sender=OrderLineItem)


def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()


post_delete.connect(update_on_delete, sender=OrderLineItem)


class DeliveryOptions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    option = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                null=False,
                                default=0)
    description = models.CharField(max_length=400, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Delivery Options"

    def __str__(self):
        return self.option
