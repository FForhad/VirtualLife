from rest_framework import permissions, status
from rest_framework.views import APIView
from apps.users.serializers import RegisterSerializer
from apps.commons.utils.response import generate_response

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return generate_response(
                success=True,
                message="User registered successfully",
                status=status.HTTP_201_CREATED,
                data={"user": RegisterSerializer(user).data},
            )
        return generate_response(
            success=False,
            message="Registration failed",
            status=status.HTTP_400_BAD_REQUEST,
            data={"errors": serializer.errors},
        )