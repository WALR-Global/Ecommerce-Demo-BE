from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import CustomTokenObtainPairView, MeApi
from users.apis.user_apis import UserDetailApi

urlpatterns = [
    path("api/token/",          CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/',  TokenRefreshView.as_view(), name='token_refresh'),
    path('api/me',              MeApi.as_view()),
]
