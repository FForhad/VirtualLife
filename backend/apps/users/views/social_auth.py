import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from apps.users.models import User
from django.conf import settings

class GoogleLoginAPIView(APIView):
    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Verify Google Token
        google_url = f"https://oauth2.googleapis.com/tokeninfo?id_token={token}"
        response = requests.get(google_url)

        if response.status_code != 200:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        user_info = response.json()

        # Ensure the token is issued for your app
        if user_info['aud'] != settings.GOOGLE_OAUTH2_CLIENT_ID:
            return Response({'error': 'Token is invalid for this app'}, status=status.HTTP_400_BAD_REQUEST)

        # Get or create user
        user, created = User.objects.get_or_create(email=user_info['email'], defaults={
            'username': user_info['email'],
            'first_name': user_info.get('given_name', ''),
            'last_name': user_info.get('family_name', ''),
        })

        # Log the user in
        login(request, user)

        return Response({
            'message': 'Login successful',
            'user': {'email': user.email, 'username': user.username}
        }, status=status.HTTP_200_OK)
