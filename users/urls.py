from django.urls import path

from users.apis import user_apis, admin_apis

urlpatterns = [
    path("users/",                        user_apis.UserListApi.as_view(), name="list"),
    path("users/create/",                 user_apis.UserCreateApi.as_view(), name="create"),
    path("users/<int:user_id>/",          user_apis.UserDetailApi.as_view(), name="detail"),
    path("users/<int:user_id>/update/",   user_apis.UserUpdateApi.as_view(), name="update"),

    path("admin/list/",                 admin_apis.AdminListApi.as_view(), name="list"),

]
