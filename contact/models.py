from django.db import models

from home.models import UpdatedAndCreated


class EmailInfo(UpdatedAndCreated):
    email_show_name = models.CharField(max_length=80,
                                       null=False,
                                       blank=False)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Email Info's"

    def __str__(self):
        return self.email
