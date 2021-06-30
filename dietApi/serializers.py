from .models import User
from rest_framework import serializers

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