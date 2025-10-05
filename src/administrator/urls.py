from django.urls import path
from .views import StudentsListView, AdminInstructorListView, AdminInstructorDetailView, StudentDetailView

urlpatterns = [
    # Преподаватели
    path('instructors/', AdminInstructorListView.as_view(), name='administrator-instructor-list'),
    path('instructors/<uuid:id>/', AdminInstructorDetailView.as_view(), name='administrator-instructor-detail'),

    # Студенты
    path('students/', StudentsListView.as_view(), name='administrator-student-list'),
    path('students/<uuid:id>/', StudentDetailView.as_view(), name='administrator-student-detail'),
]
