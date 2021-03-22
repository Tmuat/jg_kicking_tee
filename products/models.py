import uuid

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.shortcuts import reverse

from common.utils import unique_sku_generator


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.CharField(max_length=254,
                           null=True,
                           blank=True,
                           unique=True,
                           editable=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(null=False,
                            unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})


def pre_save_create_sku(sender, instance, *args, **kwargs):
    if not instance.sku:
        instance.sku = unique_sku_generator(instance)


pre_save.connect(pre_save_create_sku, sender=Product)


class ProductImage(models.Model):
    POSITION = (
        (1, 'Main Picture'),
        (2, '2nd Picture'),
        (3, '3rd Picture'),
        (4, 'Last Picture'),
    )
    image = models.ImageField(null=False,
                              blank=False,
                              upload_to='product_images')
    rank = models.IntegerField(null=False,
                               blank=False,
                               unique=True,
                               choices=POSITION)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_images',
    )

    class Meta:
        ordering = ("rank",)

    def __str__(self):
        return self.product.name


class ProductFeature(models.Model):
    feature = models.CharField(max_length=200, null=False, blank=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_features',
    )

    def __str__(self):
        return self.product.name


class ProductStock(models.Model):
    stock_quantity = models.IntegerField(null=False,
                                         blank=False,
                                         default=0)
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='product_stock',
    )

    def __str__(self):
        return self.product.name


@receiver(post_save, sender=Product)
def create_or_update_product_stock(sender, instance, created, **kwargs):
    """
    Create or update product stock.
    """
    qs_exists = ProductStock.objects.filter(
                    product=instance).exists()
    if qs_exists:
        pass
    elif created:
        ProductStock.objects.create(product=instance)
