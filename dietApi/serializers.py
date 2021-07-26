from .models import User, Measurements, PhysicalActivity
from rest_framework import serializers

class PhysicalActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalActivity
        fields = [
            "user_id",
            "activityType",
            "activityName",
            "createdAt",
            "updatedAt"
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "firstName",
            "lastName",
            "email",
            "password",
            "occupation",
            "dateOfBirth",            
            "height",
            "gender",
            "createdAt",
            "updatedAt"
        ]

class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = [
            "user",
            "MAC",
            "WC",
            "HC",
            "createdAt",
            "updatedAt"
        ]