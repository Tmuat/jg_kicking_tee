from django.contrib import admin
from .models import Order, OrderLineItem, DeliveryOptions


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_method',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid', 'user_profile')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_method',
              'delivery_cost', 'order_total', 'grand_total',
              'original_bag', 'stripe_pid', 'user_profile',
              'status')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total', 'status')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)


class CustomDeliveryOptionsAdmin(admin.ModelAdmin):
    list_display = ('option',
                    'active',
                    'price',
                    'description',
                    'delivery_sku'
                    )
    list_filter = ('option', 'price', 'description', 'active',)
    search_fields = ('option',)


admin.site.register(DeliveryOptions, CustomDeliveryOptionsAdmin)
