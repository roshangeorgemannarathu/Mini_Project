from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import dealer

class dealerAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role') # Add 'role' to the list_display
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups') # Add 'role' to the list_filter
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'role')}), # Add 'role' to the 'Personal Info' section
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'role'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name', 'role') # Add 'role' to the search_fields
    ordering = ('username',)

admin.site.register(dealer, dealerAdmin)
