from django.db import models
from apps.users.models import User  # Import custom User model
from apps.groups.models import Group  # If the post is tied to a group

class Post(models.Model):
    content = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")

    def __str__(self):
        return f"Post by {self.user.username}"

    class Meta:
        db_table = "Posts"
        ordering = ["-created_at"]  # Orders posts by the most recent first
        verbose_name = 'Post'
        verbose_name_plural = 'All Posts'


# Likes Table
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked Post {self.post.id}"

    class Meta:
        db_table = "Likes"
        ordering = ["-created_at"]  # Orders likes by the most recent first
        verbose_name = 'Like'
        verbose_name_plural = 'All Likes'


# Comments Table
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment by {self.user.username} on Post {self.post.id}"

    class Meta:
        db_table = "Comments"
        ordering = ["-created_at"]  # Orders comments by the most recent first
        verbose_name = 'Comment'
        verbose_name_plural = 'All Comments'
