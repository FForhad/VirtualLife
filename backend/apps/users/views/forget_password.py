import random
import string
import threading
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apps.users.models import User
from django.http import JsonResponse


# Function to generate a random security code
def generate_security_code(length=6):
    characters = string.digits
    security_code = ''.join(random.choice(characters) for _ in range(length))
    return security_code


# Function to send a security code email
def send_security_code_email(email, security_code):
    subject = 'Security Code for Password Reset'
    message = (
        f'Please enter this Security Code to reset your password.\n'
        f'Security Code: {security_code}\n'
        f'Thank you!'
    )
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        return True
    except Exception as e:
        return False


# Asynchronous email sender using threading
def send_email_async(user_email, security_code):
    try:
        send_security_code_email(user_email, security_code)
    except Exception as e:
        print(f"Error sending email: {str(e)}")


# API view to generate and send a security code
class SecurityCode(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username', '')
        print(username)

        try:
            # Check if the user exists
            user = User.objects.get(username=username)

            # Ensure the user has an associated email
            print(user.email)
            if not user.email:
                return JsonResponse({'status': 2, 'message': "No email associated with this user."})

            # Generate and save the security code
            security_code = generate_security_code()
            user.securitycode = security_code
            user.save()

            # Send the security code email asynchronously
            threading.Thread(target=send_email_async, args=(user.email, security_code)).start()

            return JsonResponse({'status': 3, 'message': "Security Code has been sent to your email."})

        except User.DoesNotExist:
            return JsonResponse({'status': 2, 'message': "User with this username does not exist."})


# API view to reset the user's password
class ResetPassword(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        security_code = request.data.get('securitycode', '')
        new_password = request.data.get('password', '')

        try:
            # Check if the security code is valid
            user = User.objects.get(securitycode=security_code)

            # Update the user's password and clear the security code
            user.set_password(new_password)
            user.securitycode = None
            user.save()

            return JsonResponse({'status': 3, 'message': "Password reset successfully."})

        except User.DoesNotExist:
            return JsonResponse({'status': 2, 'message': "Invalid security code."})
