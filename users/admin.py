from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile


class UserProfileAdminInline(admin.StackedInline):
    model = UserProfile


admin.site.register(UserProfile)


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileAdminInline,)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email',
                    'first_name',
                    'last_name',
                    'is_staff',
                    'is_superuser',
                    'is_active',
                    )
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_superuser','is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',
                       'first_name',
                       'last_name',
                       'password1',
                       'password2',
                       'is_staff',
                       'is_active'
                       )
                }
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
