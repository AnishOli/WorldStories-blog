from django.contrib import admin
from accounts.models import Customer

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined', 'city')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    ordering = ('-date_joined',)
    
    fieldsets = (
        ('Authentication', {
            'fields': ('email', 'password', 'is_active')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'phone_number', 'city', 'dob', 'profile_image')
        }),
        ('Authorization', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        
    )
    readonly_fields = ('date_joined', 'last_login')


# class AuthenticationGroupAdmin(BaseGroupAdmin):
#     """Custom Group Admin to categorize with authentication models"""
#     pass


# # Re-register Group with custom admin (unregister default first if needed)
# admin.site.unregister(Group)
# admin.site.register(Group, AuthenticationGroupAdmin)
