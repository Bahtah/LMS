from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from django.utils import timezone
from rest_framework.exceptions import ValidationError


@dataclass(frozen=True)
class CourseDTO:
    name_course: str
    description: Optional[str]
    course_img: Optional[str]
    start_course: datetime
    groups: list[str]
    instructor: Optional[str]

    def __post_init__(self):
        if self.start_course < timezone.now():
            raise ValidationError("Дата начала не может быть в прошлом")
        if not self.name_course.strip():
            raise ValidationError("Название курса обязательно")
