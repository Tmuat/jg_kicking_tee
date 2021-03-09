from django.contrib import admin

from .models import EmailInfo


class CustomEmailInfoAdmin(admin.ModelAdmin):
    list_display = ('email_show_name',
                    'email',
                    'created_by',
                    'created_at',
                    'updated_by',
                    'updated_at'
                    )
    list_filter = ('email',)
    search_fields = ('email',)
    readonly_fields = ['created_by', 'created_at', 'updated_by', 'updated_at']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user.email
        obj.updated_by = request.user.email
        obj.save()


admin.site.register(EmailInfo, CustomEmailInfoAdmin)
