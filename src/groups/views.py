from rest_framework.viewsets import ModelViewSet

from authorization.permissions import IsAdmin
from groups.models import Group
from groups.serializers import GroupSerializer


class GroupModelViewSet(ModelViewSet):
    permission_classes = [IsAdmin]
    serializer_class = GroupSerializer
    queryset = Group.objects.all().order_by('-start_date')
    filterset_fields = ['start_date']