from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authorization.views import LoginView, PasswordResetView, PasswordResetConfirmView, CurrentUserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('me/', CurrentUserView.as_view(), name='current-user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('password-reset/', PasswordResetView.as_view()),
    path('confirm-password-reset/', PasswordResetConfirmView.as_view()),
]
