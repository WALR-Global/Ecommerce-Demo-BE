from django.urls import path

from users.apis import user_apis

urlpatterns = [
    path("",                        user_apis.UserListApi.as_view(), name="list"),
    path("create/",                 user_apis.UserCreateApi.as_view(), name="create"),
    path("<int:user_id>/",          user_apis.UserDetailApi.as_view(), name="detail"),
    path("<int:user_id>/update/",   user_apis.UserUpdateApi.as_view(), name="update"),
]
