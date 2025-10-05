from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ('id',)

    def validate_start_date(self, value):
        from django.utils import timezone
        if value < timezone.now():
            raise serializers.ValidationError("Дата начала не может быть в прошлом")
        return value
