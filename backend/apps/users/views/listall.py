from rest_framework.views import APIView
from rest_framework import status, permissions
from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.commons.utils.response import generate_response

class UserProfileListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Retrieve all user profiles.
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return generate_response(
            success=True,
            message="User profiles fetched successfully.",
            status=status.HTTP_200_OK,
            data=serializer.data
        )
