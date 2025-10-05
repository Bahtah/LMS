from rest_framework import serializers

from authorization.models import User
from courses.dto.course_dto import CourseDTO
from courses.models import Course
from courses.services.course_service import CourseService
from groups.models import Group


class CourseSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        slug_field="group_name",
        queryset=Group.objects.all(),
        required=False
    )

    instructor = serializers.SlugRelatedField(
        slug_field="email",
        queryset=User.objects.filter(roles__name="INSTRUCTOR"),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ("id",)

    def create(self, validated_data):
        groups = validated_data.pop("groups", [])
        instructor = validated_data.pop("instructor", None)
        dto = CourseDTO(
            name_course=validated_data["name_course"],
            description=validated_data.get("description"),
            course_img=validated_data.get("course_img"),
            start_course=validated_data["start_course"],
            groups=groups,
            instructor=instructor,
        )

        return CourseService.create_course(dto)

    def update(self, instance, validated_data):
        groups = validated_data.pop("groups", None)
        instructor = validated_data.pop("instructor", None)

        dto = CourseDTO(
            name_course=validated_data.get("name_course", instance.name_course),
            description=validated_data.get("description", instance.description),
            course_img=validated_data.get("course_img", instance.course_img),
            start_course=validated_data.get("start_course", instance.start_course),
            groups=groups,
            instructor=instructor,
        )
        return CourseService.update_course(instance, dto)
