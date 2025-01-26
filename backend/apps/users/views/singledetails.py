from rest_framework import status, permissions
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.commons.utils.response import generate_response

class UserProfileRetrieveAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        """
        Retrieve a specific user profile.
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return generate_response(
                success=True,
                message="User profile retrieved successfully.",
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        except User.DoesNotExist:
            return generate_response(
                success=False,
                message="User profile not found.",
                status=status.HTTP_404_NOT_FOUND
            )
