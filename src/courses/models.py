import uuid

from django.db import models

from authorization.models import User


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=True, null=True)
    name_course = models.CharField(max_length=255, unique=True)
    course_img = models.ImageField(upload_to="courses/images/", blank=True, null=True)
    start_course = models.DateTimeField()
    groups = models.ManyToManyField("groups.Group", related_name="courses", blank=True)

    instructor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'roles__name': 'INSTRUCTOR'},
        related_name='courses_taught'
    )

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.name_course
