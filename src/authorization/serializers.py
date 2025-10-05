from rest_framework import serializers
from authorization.dto.login_dto import LoginDTO


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    def to_dto(self) -> LoginDTO:
        return LoginDTO(
            email=self.validated_data["email"],
            password=self.validated_data["password"]
        )

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    resend = serializers.BooleanField(required=False, default=False)

class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.IntegerField(required=True)
    password = serializers.CharField(write_only=True, required=True)