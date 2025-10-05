from enum import Enum

from django.db import models

class StudyFormat(models.TextChoices):
    ONLINE = 'ONLINE', 'Онлайн'
    OFFLINE = 'OFFLINE', 'Оффлайн'

class RoleType(Enum):
    INSTRUCTOR = 'INSTRUCTOR'
    STUDENT = 'STUDENT'
