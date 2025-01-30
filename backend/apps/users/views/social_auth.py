import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import login
from apps.users.models import User

class GoogleLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        access_token = request.data.get("token")
        if not access_token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Step 1: Use the access token to get user info from Google API
        user_info_url = "https://www.googleapis.com/oauth2/v3/userinfo"
        headers = {"Authorization": f"Bearer {access_token}"}
        user_info_response = requests.get(user_info_url, headers=headers)

        if user_info_response.status_code != 200:
            return Response({"error": "Invalid token or failed to fetch user info"}, status=status.HTTP_400_BAD_REQUEST)

        user_info = user_info_response.json()

        # Step 2: Get or create user
        user, created = User.objects.get_or_create(
            email=user_info["email"],
            defaults={
                "username": user_info["email"],
                "first_name": user_info.get("given_name", ""),
                "last_name": user_info.get("family_name", ""),
            },
        )

        # Log the user in
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        return Response(
            {
                "message": "Login successful",
                "user": {"email": user.email},
            },
            status=status.HTTP_200_OK,
        )
