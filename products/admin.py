from django.contrib import admin

from .models import Product, ProductImage


class CustomProductAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'sku',
                    'price',
                    'slug'
                    )
    list_filter = ('name', 'sku', 'price',)
    search_fields = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['sku', ]


admin.site.register(Product, CustomProductAdmin)


class CustomProductImageAdmin(admin.ModelAdmin):
    list_display = ('product',
                    'image',
                    )
    list_filter = ('product',)
    search_fields = ('product',)


admin.site.register(ProductImage, CustomProductImageAdmin)

