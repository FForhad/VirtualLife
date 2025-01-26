import random
import string
import logging
import threading
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apps.users.models import User
from django.http import JsonResponse


def generate_security_code(length=6):
    characters = string.digits
    security_code = ''.join(random.choice(characters) for _ in range(length))
    return security_code

def send_security_code_email(email, security_code):

    subject = 'Security Code for Password Reset'

    message = (
        f'Please enter this Security Code to reset your password.\n'
        f'Security Code: {security_code}\n'
        f'Thank you!.'
    )
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        return True
    except Exception as e:
        return False



def send_email_async(user_email, security_code):
    try:
        send_security_code_email(user_email, security_code)
    except Exception as e:
        print(f"Error sending email: {str(e)}")


class SecurityCode(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        UserId = request.data.get('userId', '')

        if not User.objects.filter(UserId=UserId).exists():
            response = {
                'status': 2,
                'message': "User with this username does not exist.",
            }
        else:
            user = User.objects.get(UserId=UserId)  # Fetch user

            # Check if the user has an email associated
            if not user.Email:
                response = {
                    'status': 2,
                    'message': "No email associated with this user.",
                }
            else:
                security_code = generate_security_code()  # Generate code
                user.SecurityCode = security_code
                user.save()

                # Create a new thread to send the email asynchronously
                threading.Thread(target=send_email_async, args=(user.Email, security_code)).start()

                response = {
                    'status': 3,
                    'message': "Security Code has been sent to your email.",
                }

        return JsonResponse(response)




class ResetPassword(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        data = request.data


        code = request.data['code']
        password = request.data['password']
        # confirmPassword = request.data['confirmPassword']

        if not User.objects.filter(SecurityCode=code).exists():
            response = {
                'status':2,
                'message': "Security Code is not valid",
            }  
        else:
            user = User.objects.get(SecurityCode=code)
            if code != user.SecurityCode:
                response = {
                    'status':2,
                    'message': "Security code do not match!",
                }  
            else:    
                user.set_password(password)
                user.SecurityCode = None
                user.save()

                response = {
                    'status':3,
                    'message': "Password reset successfully",
                }  

        return JsonResponse(response)