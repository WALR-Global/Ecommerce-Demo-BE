from typing import List

from django.db import transaction

from common.services import model_update
from common.utils import get_object
from layouts.models import FAQ


@transaction.atomic
def faq_create(*, faq_title: str,
               slug: str,
               faq_description: str = None,
               faq_type: str = None,
               ) -> FAQ:
    faq = FAQ.objects.create(faq_title=faq_title,
                             slug=slug,
                             faq_description=faq_description,
                             faq_type=faq_type,
                             )

    return faq


@transaction.atomic
def faq_update(*, faq: FAQ, data) -> FAQ:
    non_side_effect_fields: List[str] = [
        "faq_title",
        "slug",
        "faq_description",
        "faq_type",
    ]

    faq, has_updated = model_update(instance=faq, fields=non_side_effect_fields, data=data)

    return faq


@transaction.atomic
def faq_delete(*, slug: str) -> None:
    faq = get_object(FAQ, slug=slug)
    faq.delete()
    return None
