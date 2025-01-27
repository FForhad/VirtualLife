from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.serializers import LoginSerializer
from apps.commons.utils.response import generate_response
from django.core.mail import send_mail
from django.conf import settings
import threading
from apps.users.views.forget_password import generate_security_code

# Utility Function to send security code email asynchronously
def send_security_code_email_async(email, security_code):
    """
    Sends a security code to the user's email asynchronously.
    """
    subject = 'Security Code to Login'
    message = f'Please enter this Security Code to login.\nSecurity Code: {security_code}\nThank you!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        print(f"Error sending email: {str(e)}")


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        print(serializer,'+++++++++++++++')
        if serializer.is_valid():
            user = serializer.validated_data

            # If Two-Factor Authentication is enabled
            if user.twofactor:
                # Generate and send security code
                security_code = generate_security_code()
                user.security_code = security_code
                user.save()

                # Send email asynchronously
                threading.Thread(
                    target=send_security_code_email_async, args=(user.email, security_code)
                ).start()

                return generate_response(
                    success=True,
                    message="Security code sent successfully.",
                    status=status.HTTP_200_OK,
                    data={
                        'email': user.email,
                        'two_factor': user.twofactor,
                    }
                )

            # If Two-Factor Authentication is disabled
            else:
                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                access_token['id'] = user.id
                access_token['email'] = user.email
                access_token['username'] = user.username

                access_token = str(access_token)

                # Return the tokens and other relevant details
                response = generate_response(
                    success=True,
                    message="Login successful",
                    status=status.HTTP_200_OK,
                    data={
                        "access": access_token,
                        "refresh": str(refresh),
                    }
                )
                # Optionally set cookie
                response.set_cookie(
                    key="jwt",
                    value=access_token,
                    httponly=True,
                    samesite="None",
                    secure=True,
                )
                return response

        # If serializer is invalid
        return generate_response(
            success=False,
            message="Login failed",
            status=status.HTTP_400_BAD_REQUEST,
            data={"errors": serializer.errors},
        )
