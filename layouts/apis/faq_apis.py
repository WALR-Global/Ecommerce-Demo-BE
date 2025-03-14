from django.db import transaction
from django.http import Http404
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.utils import parse_search_query, get_paginated_response
from layouts.selectors import faq_list, faq_get_by_slug
from products.selectors import tag_list, tag_get_by_slug, tag_get
from products.serializers import TypeSerializer
from products.services.tag_services import tag_create, tag_update, tag_delete
from users.permissions import IsSuperAdminOrStoreOwner


class FaqListApi(APIView):
    permission_classes = [IsSuperAdminOrStoreOwner]

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        name = serializers.CharField(required=False)

    class OutputSerializer(serializers.Serializer):
        id = serializers.UUIDField()
        faq_title = serializers.CharField()
        faq_type = serializers.CharField()

    def get(self, request):
        # Extract `search` query parameter
        query_params = request.query_params
        search_query = query_params.get("search", None)

        # Parse `search` using the utility function
        filters = parse_search_query(search_query)

        # Make sure the filters are valid, if passed
        filters_serializer = self.FilterSerializer(data={**request.query_params, **filters})
        filters_serializer.is_valid(raise_exception=True)

        faqs = faq_list(filters=filters_serializer.validated_data)

        # Apply pagination
        return get_paginated_response(
            serializer_class=self.OutputSerializer,
            queryset=faqs,
            request=request,
        )


class FaqDetailApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField(required=True)
        faq_title = serializers.CharField(required=True)
        slug = serializers.CharField(required=True)
        faq_description = serializers.CharField(required=True)
        faq_type = serializers.CharField(required=True)
        issued_by = serializers.CharField()
        translated_languages = serializers.JSONField()

    def get(self, request, slug):
        faq = faq_get_by_slug(slug)

        if faq is None:
            raise Http404

        data = self.OutputSerializer(faq).data

        return Response(data)


class FaqCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=True)
        slug = serializers.CharField(required=True)
        details = serializers.CharField(required=True, allow_blank=True, allow_null=True)
        image = serializers.JSONField(required=True, allow_null=True)
        icon = serializers.JSONField(required=True, allow_null=True)
        type_id = serializers.IntegerField(required=True, allow_null=True)

    class OutputSerializer(serializers.Serializer):
        id = serializers.UUIDField(required=True)
        slug = serializers.CharField(required=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tag = tag_create(
            **serializer.validated_data
        )

        data = self.OutputSerializer(tag).data

        return Response(data)


class FaqUpdateApi(APIView):

    @transaction.atomic
    def put(self, request, tag_id):
        serializer = TagCreateApi.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tag = tag_get(tag_id)

        if tag is None:
            raise Http404

        tag = tag_update(tag=tag, data=serializer.validated_data)

        # Note: This shows a possible reusability for serializers between APIs
        # Usually, this is how we approach things, when building APIs at first
        # But at the very moment when we need to make a change to the output,
        # that's specific to this API, we'll introduce a separate OutputSerializer just for this API
        data = TagCreateApi.OutputSerializer(tag).data

        return Response(data)


class FaqDeleteApi(APIView):
    @staticmethod
    def delete(request, tag_id: str):
        tag_delete(tag_id=tag_id)

        return Response(
            {"detail": "Tag successfully deleted."},
            status=status.HTTP_204_NO_CONTENT  # 204 for successful delete with no content
        )
