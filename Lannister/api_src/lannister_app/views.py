from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import CreateUserSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):

    """Registers user to the server. Input should be in the format:
    {"username":"name",
    "email":"email@domain.com",
    "roles":"["role1","role2"]",
    "password": "password"}я
    """

    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        success = {
            "message": f"Successfully registered user: [{request.data['username']}]"
        }
        return Response(success)
    return Response(serializer.errors, status=400)
