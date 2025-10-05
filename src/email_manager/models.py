import uuid
from datetime import timedelta

from django.db import models
from django.utils import timezone

from authorization.models import User


class EmailManager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='email_id')
    user_id = models.UUIDField()
    message_type = models.CharField(max_length=255)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "emails"

    @classmethod
    def can_send_letter(cls, user_id, message_type):
        last_email_sent = cls.objects.filter(user_id=user_id, message_type=message_type).last()
        if last_email_sent and (timezone.now() - last_email_sent.sent_at) < timedelta(seconds=30):
            return False
        return True


class PasswordResetCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reset_codes")
    code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = "password_reset_codes"

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)
