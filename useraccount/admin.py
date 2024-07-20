from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'identifier_name', 'email', 'telegram_id', 'is_staff',
                    'vpn_link', 'fragment', 'month', 'user', 'type']

    # Removing 'first_name', 'last_name' from custom fieldsets since they are already in UserAdmin.fieldsets
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('identifier_name', 'telegram_id', 'vpn_link', 'fragment', 'month', 'user', 'type')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('identifier_name', 'telegram_id', 'vpn_link', 'fragment', 'month', 'user', 'type')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
