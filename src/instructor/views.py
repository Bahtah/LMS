from rest_framework.viewsets import ModelViewSet

from authorization.permissions import IsInstructor


class InstructorModelViewSet(ModelViewSet):
    permission_classes = [IsInstructor]
