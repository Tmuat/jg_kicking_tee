from django.contrib import admin

from .models import Product, ProductImage, ProductFeature, ProductStock


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductFeatureInline(admin.StackedInline):
    model = ProductFeature


class ProductStockInline(admin.StackedInline):
    model = ProductStock


class CustomProductAdmin(admin.ModelAdmin):
    inlines = (ProductStockInline, ProductFeatureInline, ProductImageInline)
    list_display = ('name',
                    'sku',
                    'price',
                    'slug',
                    )
    list_filter = ('name', 'sku', 'price',)
    search_fields = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['sku', ]


admin.site.register(Product, CustomProductAdmin)
