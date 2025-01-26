from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import os
from django.contrib.auth.hashers import make_password, check_password

# Manager for User model
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, username, password, **extra_fields)

# Path for profile picture uploads
def user_directory_path(instance, filename):
    return os.path.join('profile_pics', str(instance.id), filename)

# Validate image size
def validate_image(image):
    filesize = image.file.size
    limit_mb = 5
    if filesize > limit_mb * 1024 * 1024:
        raise ValidationError(f"Max size of the profile picture is {limit_mb}MB.")

class CustomPasswordField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 128  
        super(CustomPasswordField, self).__init__(*args, **kwargs)

    def set_password(self, raw_password):
        self.value = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.value)
    
# Custom User model
class User(AbstractBaseUser, PermissionsMixin):
    password = None
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = CustomPasswordField(verbose_name='password')
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True,
        validators=[
            validate_image,
            FileExtensionValidator(['jpg', 'jpeg', 'png'])
        ]
    )
    twofactor = models.BooleanField(default=False)
    securitycode = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Users"
        ordering = ["-created_at"]
        verbose_name = 'User'
        verbose_name_plural = 'All Users'

    def save(self, *args, **kwargs):
        if self.pk is None or self._state.adding:
            if self.password and not self.password.startswith('pbkdf2_sha256$'):
                self.set_password(self.password)
        super().save(*args, **kwargs)
