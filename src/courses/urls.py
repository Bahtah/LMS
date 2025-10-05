from django.urls import path, include
from rest_framework.routers import DefaultRouter

from courses.views import CourseModelViewSet

router = DefaultRouter()
router.register(r'', CourseModelViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
]