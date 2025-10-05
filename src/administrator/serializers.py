from rest_framework import serializers

from administrator.dto.instructor_dto import InstructorDTO
from administrator.dto.student_dto import StudentDTO
from administrator.enums import StudyFormat
from administrator.services.instructor_service import InstructorService
from administrator.services.student_service import StudentService
from authorization.models import User, Role
from groups.models import Group


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("id", "name")


class CurrentUserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number',
                  'specialization', 'study_format', 'is_active', 'has_paid', 'roles')


class AdminInstructorSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=False, default=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'specialization', 'is_active')
        read_only_fields = ('id',)

    def create(self, validated_data):
        dto = InstructorDTO(
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            phone_number=validated_data.get('phone_number'),
            specialization=validated_data.get('specialization'),
            is_active=validated_data.get('is_active', True)
        )
        return InstructorService.create_instructor(dto)

    def update(self, instance, validated_data):
        dto = InstructorDTO(
            email=validated_data.get('email', instance.email),
            first_name=validated_data.get('first_name', instance.first_name),
            last_name=validated_data.get('last_name', instance.last_name),
            phone_number=validated_data.get('phone_number', instance.phone_number),
            specialization=validated_data.get('specialization', instance.specialization),
            is_active=validated_data.get('is_active', instance.is_active)
        )
        return InstructorService.update_instructor(instance, dto)


class AdminStudentSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=False, default=True)
    has_paid = serializers.BooleanField(required=False, default=False)

    groups = serializers.SlugRelatedField(
        many=True,
        slug_field="group_name",
        queryset=Group.objects.all(),
        required=False
    )

    study_format = serializers.ChoiceField(
        choices=StudyFormat.choices,
        required=False,
        allow_blank=True
    )

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'phone_number', 'study_format', 'groups', 'is_active', 'has_paid')
        read_only_fields = ('id',)

    def create(self, validated_data):
        group_names = None
        if "groups" in validated_data:
            group_names = [g.group_name for g in validated_data.pop("groups")]

        dto = StudentDTO(
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            phone_number=validated_data.get('phone_number'),
            study_format=validated_data.get('study_format'),
            is_active=validated_data.get('is_active', True),
            has_paid=validated_data.get('has_paid', False),
            group_names=group_names
        )
        return StudentService.create_student(dto)

    def update(self, instance, validated_data):
        group_names = [g.group_name for g in validated_data.pop('groups', instance.groups.all())] if 'groups' in validated_data else None
        dto = StudentDTO(
            email=validated_data.get('email', instance.email),
            first_name=validated_data.get('first_name', instance.first_name),
            last_name=validated_data.get('last_name', instance.last_name),
            phone_number=validated_data.get('phone_number', instance.phone_number),
            study_format=validated_data.get('study_format', instance.study_format),
            is_active=validated_data.get('is_active', instance.is_active),
            has_paid=validated_data.get('has_paid', instance.has_paid),
            group_names=group_names
        )
        return StudentService.update_student(instance, dto)