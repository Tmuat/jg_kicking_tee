import uuid

from django.db import models
from django.db.models.signals import pre_save

from common.utils import unique_sku_generator


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(null=False,
                            unique=True)

    def __str__(self):
        return self.name


def pre_save_create_sku(sender, instance, *args, **kwargs):
    if not instance.sku:
        instance.sku = unique_sku_generator(instance)


pre_save.connect(pre_save_create_sku, sender=Product)


class ProductImage(models.Model):
    image = models.ImageField(null=True, blank=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_images',
    )

    def __str__(self):
        return self.product.name
