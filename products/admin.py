from django.contrib import admin

from .models import Product


class CustomProductAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'sku',
                    'price',
                    )
    list_filter = ('name', 'sku', 'price',)
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Product, CustomProductAdmin)
