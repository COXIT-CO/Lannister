from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Bonus_request, Bonus_request_history, User


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "roles", "is_staff", "is_active"]


class BonusRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus_request
        fields = ["id", "creator", "reviewer", "bonus_type", "description", "status"]


class BonusRequestHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus_request_history
        fields = [
            "id",
            "request_id",
            "date_created",
            "date_approved",
            "date_rejected",
            "date_done",
            "date_changed",
            "date_payment",
        ]
