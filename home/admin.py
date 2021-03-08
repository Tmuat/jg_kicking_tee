from django.contrib import admin


from .models import Image


class CustomImageAdmin(admin.ModelAdmin):
    list_display = ('image_location',
                    'active',
                    'image',
                    'created_by',
                    'created_at'
                    )
    list_filter = ('image_location', 'active',)
    search_fields = ('name',)
    ordering = ('image_location',)
    readonly_fields = ['created_by', 'created_at', 'updated_by', 'updated_at']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user.username
        obj.updated_by = request.user.username
        obj.save()


admin.site.register(Image, CustomImageAdmin)
