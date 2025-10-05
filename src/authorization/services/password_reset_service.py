from rest_framework.exceptions import ValidationError

from authorization.dto.password_reset_dto import PasswordResetResultDTO, PasswordResetRequestDTO, \
    PasswordResetConfirmDTO
from authorization.helpers import generate_code
from authorization.models import User
from email_manager.models import PasswordResetCode
from email_manager.services import EmailService


class PasswordResetService:

    @staticmethod
    def create_reset_code(dto: PasswordResetRequestDTO) -> PasswordResetResultDTO:
        try:
            user = User.objects.get(email=dto.email)
        except User.DoesNotExist:
            raise ValidationError({"email": "Пользователь не найден"})

        last_code = PasswordResetCode.objects.filter(user=user).order_by('-created_at').first()

        if dto.resend and last_code and not last_code.confirmed and not last_code.is_expired():
            reset_code = last_code.code
        else:
            PasswordResetCode.objects.filter(user=user, confirmed=False, completed=False).update(completed=True)
            reset_code = generate_code()
            PasswordResetCode.objects.create(user=user, code=reset_code)

        EmailService.send_password_reset(user.id, user.email, reset_code)

        return PasswordResetResultDTO(success=True, message="Password reset code sent")

    @staticmethod
    def confirm_reset(dto: PasswordResetConfirmDTO) -> PasswordResetResultDTO:
        try:
            user = User.objects.get(email=dto.email)
        except User.DoesNotExist:
            raise ValidationError({"email": "Пользователь не найден"})

        password_reset = PasswordResetCode.objects.filter(
            user=user,
            confirmed=False,
            completed=False,
        ).order_by('-created_at').first()

        if not password_reset:
            raise ValidationError({"confirmation_code": "Код не найден"})

        if password_reset.is_expired():
            password_reset.completed = True
            password_reset.save()
            raise ValidationError({"confirmation_code": "Срок действия кода истек"})

        if password_reset.code != dto.confirmation_code:
            raise ValidationError({"confirmation_code": "Неверный код"})

        user.set_password(dto.new_password)
        user.save()

        password_reset.confirmed = True
        password_reset.completed = True
        password_reset.save()

        return PasswordResetResultDTO(success=True, message="Password has been reset")
