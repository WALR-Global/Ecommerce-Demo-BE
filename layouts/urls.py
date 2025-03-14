from django.urls import path

from layouts.apis import faq_apis

urlpatterns = [
    path('faqs/', faq_apis.FaqListApi.as_view()),
    path('faqs/create', faq_apis.FaqCreateApi.as_view()),
    path('faqs/<str:slug>', faq_apis.FaqDetailApi.as_view()),
    path('faqs/<str:slug>/update', faq_apis.FaqUpdateApi.as_view()),
    path('faqs/<str:slug>/delete', faq_apis.FaqDeleteApi.as_view()),

]
