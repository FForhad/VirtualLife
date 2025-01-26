from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'twofactor', 'created_at')
    fields = ('username', 'email', 'password', 'first_name', 'last_name', 'bio', 'profile_picture', 'twofactor', 'securitycode', 'is_active', 'is_staff', 'is_superuser', 'groups')

admin.site.register(User, CustomUserAdmin)
