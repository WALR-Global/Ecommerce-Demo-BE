from django.urls import path

from systemconfig.apis import settings_apis

urlpatterns = [
    path('settings/', settings_apis.get_settings, name='get_settings'),
    # path('attachments', file_upload_views.upload_file, name='upload_file'),
]
