from django.db import models
from apps.users.models import User  # Import custom User model

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_groups")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Groups"
        ordering = ["-created_at"]  # Orders groups by the most recent first
        verbose_name = 'Group'
        verbose_name_plural = 'All Groups'


class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="group_members")
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('group', 'user')
        db_table = "GroupMembers"
        ordering = ["joined_at"]  # Orders members by the date they joined
        verbose_name = 'Group Member'
        verbose_name_plural = 'All Group Members'

    def __str__(self):
        return f"{self.user.username} in Group {self.group.name}"
