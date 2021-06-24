from django.contrib import admin

from .models import LandingImage, Testimonial, InstructionalVideo


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
            obj.created_by = request.user.email
        obj.updated_by = request.user.email
        obj.save()


admin.site.register(LandingImage, CustomImageAdmin)


class CustomTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'active',
                    'testimonial',
                    'image',
                    'created_by',
                    'created_at'
                    )
    list_filter = ('name', 'active',)
    search_fields = ('name',)
    readonly_fields = ['created_by', 'created_at', 'updated_by', 'updated_at']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user.email
        obj.updated_by = request.user.email
        obj.save()


admin.site.register(Testimonial, CustomTestimonialAdmin)


class CustomVideoAdmin(admin.ModelAdmin):
    list_display = ('video',
                    'created_by',
                    'created_at'
                    )
    readonly_fields = ['created_by', 'created_at', 'updated_by', 'updated_at']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user.email
        obj.updated_by = request.user.email
        obj.save()


admin.site.register(InstructionalVideo, CustomVideoAdmin)
