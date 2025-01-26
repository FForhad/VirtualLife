from rest_framework import status, permissions
from rest_framework.views import APIView
from apps.users.serializers import UserSerializer
from apps.commons.utils.response import generate_response

class UserProfileCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """
        Create a new user profile.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return generate_response(
                success=True,
                message="User profile created successfully.",
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )
        return generate_response(
            success=False,
            message="Invalid data provided.",
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )
