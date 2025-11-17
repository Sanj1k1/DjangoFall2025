from django.contrib import admin
from apps.customusers.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'phone',
        'city',
        'country',
        'department',
        'role',
        'birth_date',
        'salary',
        'is_active',
        'is_staff',
        'date_joined',
        'last_login',
    )
    list_filter = ('role', 'is_active', 'is_staff', 'department')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'phone')
    ordering = ('id',)
