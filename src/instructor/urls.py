from django.urls import include, path
from rest_framework.routers import DefaultRouter
from instructor.views import InstructorModelViewSet

router = DefaultRouter()
router.register(r'', InstructorModelViewSet, basename='instructor')

urlpatterns = [
    path('', include(router.urls)),
]