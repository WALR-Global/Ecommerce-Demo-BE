from typing import List

from django.db import transaction

from common.services import model_update
from common.utils import get_object
from products.models import Attribute


@transaction.atomic
def attribute_create(*, name: str,
                     slug: str,
                     ) -> Attribute:
    attribute = Attribute.objects.create(name=name,
                                         slug=slug,
                                         )

    return attribute


@transaction.atomic
def attribute_update(*, attribute: Attribute, data) -> Attribute:
    non_side_effect_fields: List[str] = [
        "name",
        "slug",
    ]

    attribute, has_updated = model_update(instance=attribute, fields=non_side_effect_fields, data=data)

    # some additional task
    attribute.type_id = data.get("type_id")
    attribute.save()

    return attribute


@transaction.atomic
def attribute_delete(*, slug: str) -> None:
    attribute = get_object(Attribute, slug=slug)
    attribute.delete()
    return None
