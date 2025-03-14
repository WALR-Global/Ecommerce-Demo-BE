from typing import Optional

from django.db.models import QuerySet

from common.utils import get_object
from layouts.models import FAQ


def faq_list(*, filters=None) -> QuerySet[FAQ]:
    filters = filters or {}

    qs = FAQ.objects.all()

    return qs


def faq_get_by_slug(slug) -> Optional[FAQ]:
    faq = get_object(FAQ, slug=slug)

    return faq
