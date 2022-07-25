
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CreateUserSerializer
from loguru import logger

# from django.shortcuts import render

logger.add(
    "loguru.log",
    level="INFO",
    format="{time} {level} {message}",
    retention="30 days",
    serialize=True,  # json format of logs
)

logger.info("Information message")

@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):

    """Registers user to the server. Input should be in the format:
    {"username":"name",
    "email":"email@domain.com",
    "password": "password"}
    """

    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        success = {
            "message": f"Successfully registered user:" f" [{request.data['username']}]"
        }
        return Response(success)
    return Response(serializer.errors, status=400)

