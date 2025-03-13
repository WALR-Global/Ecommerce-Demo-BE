from django.urls import path

from products.apis import type_apis, tag_apis, category_apis, attribute_apis, manufacturer_apis

urlpatterns = [
    path('types/', type_apis.TypeListApi.as_view()),

    path('categories/', category_apis.CategoryListApi.as_view()),
    path('categories/create', category_apis.CategoryCreateApi.as_view()),
    path('categories/<slug:slug>', category_apis.CategoryDetailApi.as_view()),
    path('categories/<str:category_id>/update', category_apis.CategoryUpdateApi.as_view()),
    path('categories/<str:category_id>/delete', category_apis.CategoryDeleteApi.as_view()),

    path('tags/', tag_apis.TagListApi.as_view()),
    path('tags/create', tag_apis.TagCreateApi.as_view()),
    path('tags/<str:slug>', tag_apis.TagDetailApi.as_view()),
    path('tags/<str:tag_id>/update', tag_apis.TagUpdateApi.as_view()),
    path('tags/<str:tag_id>/delete', tag_apis.TagDeleteApi.as_view()),

    path('attributes/', attribute_apis.AttributeListApi.as_view()),
    path('attributes/create', attribute_apis.AttributeCreateApi.as_view()),
    path('attributes/<str:slug>', attribute_apis.AttributeDetailApi.as_view()),
    path('attributes/<str:attribute_id>/update', attribute_apis.AttributeUpdateApi.as_view()),
    path('attributes/<str:slug>/delete', attribute_apis.AttributeDeleteApi.as_view()),

    path('manufacturers/', manufacturer_apis.ManufacturerListApi.as_view()),
    path('manufacturers/create', manufacturer_apis.ManufacturerCreateApi.as_view()),
    path('manufacturers/<str:slug>', manufacturer_apis.ManufacturerDetailApi.as_view()),
    path('manufacturers/<str:attribute_id>/update', manufacturer_apis.ManufacturerUpdateApi.as_view()),
    path('manufacturers/<str:slug>/delete', manufacturer_apis.ManufacturerDeleteApi.as_view()),

]
