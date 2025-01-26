# groups/admin.py
from django.contrib import admin
from .models import Group, GroupMember

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin', 'created_at', 'updated_at', 'description')  # Display relevant fields
    search_fields = ('name', 'admin__username')  # Enable search by group name and admin (user)
    list_filter = ('created_at', 'admin')  # Filter by creation date and admin (user)
    ordering = ('-created_at',)  # Order by creation date, newest first

class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('group', 'user', 'joined_at')  # Display relevant fields
    search_fields = ('user__username', 'group__name')  # Enable search by user and group name
    list_filter = ('joined_at', 'group')  # Filter by join date and group
    ordering = ('-joined_at',)  # Order by join date, newest first

admin.site.register(Group, GroupAdmin)
admin.site.register(GroupMember, GroupMemberAdmin)
