import urllib.parse
import uuid

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from email_manager.enums import MessageType
from email_manager.models import EmailManager


class EmailService:

    @staticmethod
    def send_account_creation(user_id: uuid.UUID, user_email: str, first_name: str | None, password: str, role: str):
        if not EmailManager.can_send_letter(user_id, "ACCOUNT_CREATION"):
            return False

        mail_subject = 'Ваш аккаунт в PyAcademy'
        html_message = render_to_string('email_manager/account_creation.html', {
            'user_email': user_email,
            'first_name': first_name,
            'password': password,
            'role': role
        })
        plain_message = strip_tags(html_message)
        email = EmailMultiAlternatives(
            subject=mail_subject,
            body=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user_email]
        )
        email.attach_alternative(html_message, "text/html")
        email.send()

        EmailManager.objects.create(user_id=user_id, message_type=MessageType.ACCOUNT_CREATION.value)
        return True

    @staticmethod
    def send_password_reset(user_id: uuid.UUID, user_email: str, confirmation_code: int):
        url_encoded_email = urllib.parse.quote(user_email)

        mail_subject = 'Восстановление пароля'
        html_message = render_to_string('email_manager/confirm_reset_password.html', {
            'user_email': user_email,
            'email': url_encoded_email,
            'domain': settings.CLIENT_DOMAIN,
            'reset_code': confirmation_code,
        })
        plain_message = strip_tags(html_message)
        email = EmailMultiAlternatives(
            subject=mail_subject,
            body=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user_email]
        )
        email.attach_alternative(html_message, "text/html")
        email.send()

        EmailManager.objects.create(user_id=user_id, message_type=MessageType.PASSWORD_RESET.value)
