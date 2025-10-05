from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from administrator.serializers import CurrentUserSerializer
from authorization.dto.password_reset_dto import PasswordResetRequestDTO, PasswordResetConfirmDTO
from authorization.serializers import LoginSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from authorization.services.login_service import AuthService
from authorization.services.password_reset_service import PasswordResetService


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = serializer.to_dto()
        tokens = AuthService.login(dto)

        return Response(tokens)


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CurrentUserSerializer(request.user)
        return Response(serializer.data)


class PasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = PasswordResetRequestDTO(
            email=serializer.validated_data["email"],
            resend=serializer.validated_data.get("resend", False),
        )

        result = PasswordResetService.create_reset_code(dto)
        return Response({"detail": result.message}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = PasswordResetConfirmDTO(
            email=serializer.validated_data["email"],
            confirmation_code=serializer.validated_data["confirmation_code"],
            new_password=serializer.validated_data["password"],
        )

        result = PasswordResetService.confirm_reset(dto)
        return Response({"detail": result.message}, status=status.HTTP_200_OK)


