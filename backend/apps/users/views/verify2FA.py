
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User
from apps.commons.utils.response import generate_response
from rest_framework import status

class VerifySecurityCode(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        security_code = request.data.get('securitycode')

        # Validate inputs
        if not email or not security_code:
            return generate_response(
                success=False,
                message="User ID and security code are required.",
                status=status.HTTP_400_BAD_REQUEST
            )

        # Fetch user
        user = User.objects.filter(email=email).first()
        if user is None:
            return generate_response(
                success=False,
                message="User not found",
                status=status.HTTP_404_NOT_FOUND
            )

        # Verify security code
        if user.securitycode != security_code:
            return generate_response(
                success=False,
                message="Invalid security code",
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Security code verified; clear it
        user.securitycode = None
        user.save()

        # Generate tokens
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        access_token['id'] = user.id
        access_token['email'] = user.email
        access_token['username'] = user.username

        access_token = str(access_token)

        response = generate_response(
            success=True,
            message="Login successful",
            status=status.HTTP_200_OK,
            data={
                "access": access_token,
                "refresh": str(refresh),
            }
        )

        # Set JWT token in HTTP-only cookie
        response.set_cookie(
            key="jwt",
            value=access_token,
            httponly=True,
            samesite="None",
            secure=True,
        )

        return response
