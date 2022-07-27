from rest_framework import serializers
from django.contrib.auth import get_user_model
from flights.models import Booking, Flight
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["destination", "time", "price", "id"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "id"]


class BookingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "passengers", "id"]


class UpdateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["date", "passengers"]


class UserRegistrationSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        new_user = User(**validated_data)
        new_user.set_password(password)
        new_user.save()
        return validated_data
