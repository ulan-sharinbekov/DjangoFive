from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from _auth.views import UserCreateAPIView, UserUpdateAPIView

urlpatterns = [
    path('signup/', UserCreateAPIView.as_view()),
    path('user/<int:pk>', UserUpdateAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
© 2022 GitHub, Inc.
Terms
Privacy
Se
