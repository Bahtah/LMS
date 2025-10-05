from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

from authorization.dto.login_dto import LoginDTO


class AuthService:
    @staticmethod
    def login(dto: LoginDTO):
        user = authenticate(username=dto.email, password=dto.password)
        if not user:
            raise AuthenticationFailed("Неверные учетные данные")

        refresh = RefreshToken.for_user(user)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }
