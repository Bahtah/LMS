from django.urls import path, include

urlpatterns = [
    path('auth/', include('authorization.urls')),
    path('admin/', include('administrator.urls')),
    path('groups/', include('groups.urls')),
    path('courses/', include('courses.urls')),
    path('instructor/', include('instructor.urls')),
]
