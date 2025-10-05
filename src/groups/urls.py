from django.urls import include, path
from rest_framework.routers import DefaultRouter

from groups.views import GroupModelViewSet

router = DefaultRouter()
router.register(r'', GroupModelViewSet, basename='groups')

urlpatterns = [
    path('', include(router.urls)),
]