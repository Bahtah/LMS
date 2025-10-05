from rest_framework import generics
from django_filters import rest_framework as filters

from authorization.models import User
from authorization.permissions import IsAdmin
from .enums import StudyFormat
from .serializers import AdminInstructorSerializer, AdminStudentSerializer


# Преподаватели
class AdminInstructorListView(generics.ListCreateAPIView):
    """Создание и список преподавателей"""
    permission_classes = [IsAdmin]
    queryset = User.objects.filter(roles__name="INSTRUCTOR")
    serializer_class = AdminInstructorSerializer

class AdminInstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Получение, обновление и удаление преподавателя"""
    permission_classes = [IsAdmin]
    queryset = User.objects.filter(roles__name="INSTRUCTOR")
    serializer_class = AdminInstructorSerializer
    lookup_field = 'id'

# Студенты
class StudentFilter(filters.FilterSet):
    """Фильтр студентов по формату обучения"""
    study_format = filters.ChoiceFilter(choices=StudyFormat.choices)

    class Meta:
        model = User
        fields = ['study_format']

class StudentsListView(generics.ListCreateAPIView):
    """Создание, список и фильтрация студентов"""
    permission_classes = [IsAdmin]
    serializer_class = AdminStudentSerializer
    queryset = User.objects.filter(roles__name="STUDENT")
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = StudentFilter

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Получение, обновление и удаление студента"""
    permission_classes = [IsAdmin]
    serializer_class = AdminStudentSerializer
    queryset = User.objects.filter(roles__name="STUDENT")
    lookup_field = 'id'
