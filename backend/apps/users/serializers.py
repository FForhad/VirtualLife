from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True, required=False, allow_blank=False)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'first_name', 'last_name', 
            'bio', 'profile_picture', 'profile_picture_url', 
            'created_at', 'updated_at', 'password',
            'twofactor', 'securitycode'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_profile_picture_url(self, obj):
        request = self.context.get('request')
        if obj.profile_picture and hasattr(obj.profile_picture, 'url'):
            return request.build_absolute_uri(obj.profile_picture.url) if request else obj.profile_picture.url
        return None
    

    def create(self, validated_data):
        """Handle user creation with password hashing"""
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        
        if password:
            user.set_password(password)  # Hash password before saving
            user.save()

        return user

    def update(self, instance, validated_data):
        """Handle user update with password change"""
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)  # Hash password before saving
        return super().update(instance, validated_data)
