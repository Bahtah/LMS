import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from administrator.enums import StudyFormat
from .managers import UserManager

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "roles"

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='user_id')
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    password = models.CharField(max_length=128)

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    specialization = models.CharField(max_length=255, null=True, blank=True)

    study_format = models.CharField(
        max_length=255,
        choices=StudyFormat.choices,
        null=True,
        blank=True
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    has_paid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    roles = models.ManyToManyField(Role, related_name='users', blank=True)
    groups = models.ManyToManyField('groups.Group', related_name='users', blank=True)
    courses = models.ManyToManyField('courses.Course', related_name='users', blank=True)

    class Meta:
        db_table = "users"

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email