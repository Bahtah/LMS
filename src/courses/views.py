from rest_framework.viewsets import ModelViewSet

from authorization.permissions import IsAdmin
from courses.models import Course
from courses.serializers import CourseSerializer


class CourseModelViewSet(ModelViewSet):
    permission_classes = [IsAdmin]
    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by("-start_course")
    filterset_fields = ["start_course"]
    search_fields = ["name_course"]
