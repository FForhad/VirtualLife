from rest_framework import permissions, status
from rest_framework.views import APIView
from apps.users.models import User
from apps.commons.utils.response import generate_response

class UserProfileDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        """
        Delete a user profile.
        """
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return generate_response(
                success=True,
                message="User profile deleted successfully.",
                status=status.HTTP_204_NO_CONTENT
            )
        except User.DoesNotExist:
            return generate_response(
                success=False,
                message="User profile not found.",
                status=status.HTTP_404_NOT_FOUND
            )
