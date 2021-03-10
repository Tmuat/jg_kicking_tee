from django.contrib import admin

from .models import Product, ProductImage, ProductFeature


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


class CustomProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('product',
                    'feature',
                    )
    list_filter = ('product',)
    search_fields = ('feature',)


admin.site.register(ProductFeature, CustomProductFeatureAdmin)
