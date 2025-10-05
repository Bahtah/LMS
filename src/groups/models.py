import uuid

from django.db import models

class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=True, null=True)
    group_name = models.CharField(max_length=255, unique=True)
    group_image = models.ImageField(upload_to='groups/images/', blank=True, null=True)
    start_date = models.DateTimeField()

    class Meta:
        db_table = "groups"

    def __str__(self):
        return self.group_name