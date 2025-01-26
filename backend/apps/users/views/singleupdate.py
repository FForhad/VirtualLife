from rest_framework import status, permissions
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.commons.utils.response import generate_response

class UserProfileUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        """
        Update a user profile.
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return generate_response(
                    success=True,
                    message="User profile updated successfully.",
                    status=status.HTTP_200_OK,
                    data=serializer.data
                )
            return generate_response(
                success=False,
                message="Invalid data provided.",
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )
        except User.DoesNotExist:
            return generate_response(
                success=False,
                message="User profile not found.",
                status=status.HTTP_404_NOT_FOUND
            )
