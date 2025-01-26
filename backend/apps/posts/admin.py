# posts/admin.py
from django.contrib import admin
from .models import Post, Like, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'created_at', 'updated_at', 'content')  # Display relevant fields
    search_fields = ('content', 'user__username')  # Enable search by post content and user
    list_filter = ('created_at', 'user')  # Filter by creation date and user
    ordering = ('-created_at',)  # Order by creation date, newest first
    readonly_fields = ('created_at', 'updated_at')  # Make creation and update timestamps readonly

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')  # Display relevant fields
    search_fields = ('user__username', 'post__id')  # Enable search by user and post ID
    list_filter = ('created_at', 'user')  # Filter by user and creation date
    ordering = ('-created_at',)  # Order by creation date, newest first

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'updated_at', 'content')  # Display relevant fields
    search_fields = ('content', 'user__username', 'post__id')  # Enable search by content, user, and post
    list_filter = ('created_at', 'user')  # Filter by user and creation date
    ordering = ('-created_at',)  # Order by creation date, newest first
    readonly_fields = ('created_at', 'updated_at')  # Make creation and update timestamps readonly

admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
