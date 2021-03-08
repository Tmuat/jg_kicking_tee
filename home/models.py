import uuid

from django.db import models


class UpdatedAndCreated(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100,
                                  null=True,
                                  blank=True)
    updated_by = models.CharField(max_length=100,
                                  null=True,
                                  blank=True)

    class Meta:
        abstract = True


class Image(UpdatedAndCreated):
    image_location = models.CharField(max_length=50,
                                      null=False,
                                      blank=False)
    image = models.ImageField(upload_to="images/",
                              null=True,
                              blank=False)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Images"
        ordering = ['created_at']

    def __str__(self):
        return self.image_location
