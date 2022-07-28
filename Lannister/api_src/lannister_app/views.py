from loguru import logger
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bonus_request, Bonus_request_history, User
from .serializers import (BonusRequestHistorySerializer,
                          BonusRequestSerializer, CreateUserSerializer,
                          GetUserSerializer)

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
        if request.data["slack_id"]:
            User.objects.filter(id=request.data["id"]).update(slack_id=request.data["slack_id"])
        success = {
            "message": f"Successfully registered user:" f" [{request.data['username']}]"
        }
        return Response(success)
    return Response(serializer.errors, status=400)


# returns all requests
class BonusRequestList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = Bonus_request.objects.all()
    serializer_class = BonusRequestSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# returns/update/deletes single request
class BonusRequestSingle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = Bonus_request.objects.all()
    serializer_class = BonusRequestSerializer


# returns all requests of specific worker
class WorkerBonusRequestList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        worker_requests = Bonus_request.objects.filter(creator=pk)
        serializer = BonusRequestSerializer(worker_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# returns all requests of specific reviewer
class ReviewerBonusRequestList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        reviewer_requests = Bonus_request.objects.filter(reviewer=pk)
        serializer = BonusRequestSerializer(reviewer_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# returns all bonus_request_history objects
class BonusRequestHistoryList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = Bonus_request_history.objects.all()
    serializer_class = BonusRequestHistorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# returns/update/deletes single bonus_request_history object
class BonusRequestHistorySingle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = Bonus_request_history.objects.all()
    serializer_class = BonusRequestHistorySerializer


# returns all users
class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = User.objects.all()
    serializer_class = GetUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# returns/update/deletes info about single user
class UserSingle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = GetUserSerializer


# returns all reviewers
class ReviewerList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.filter(roles__contains=["reviewer"])
    serializer_class = GetUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# returns/update/deletes single reviewer
class ReviewerSingle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.filter(roles__contains=["reviewer"])
    serializer_class = GetUserSerializer


# returns all workers
class WorkerList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.filter(roles__contains=["worker"])
    serializer_class = GetUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# returns/update/deletes single worker
class WorkerSingle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.filter(roles__contains=["worker"])
    serializer_class = GetUserSerializer


# returns user id by slack id
class UserSlackId(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, slack_id):
        worker_requests = User.objects.filter(slack_id=slack_id).first()
        return Response(worker_requests.json(), status=status.HTTP_200_OK)
