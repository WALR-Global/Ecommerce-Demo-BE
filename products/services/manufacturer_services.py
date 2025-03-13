from typing import List

from django.db import transaction

from common.services import model_update
from common.utils import get_object
from products.models import Manufacturer


@transaction.atomic
def manufacture_create(*, name: str,
                       slug: str,
                       description: str = None,
                       image: str = None,
                       cover_image: str = None,
                       icon: str = None,
                       website: str = None,
                       ) -> Manufacturer:
    manufacture = Manufacturer.objects.create(name=name,
                                              slug=slug,
                                              description=description,
                                              image=image,
                                              cover_image=cover_image,
                                              icon=icon,
                                              website=website,
                                              )

    return manufacture


@transaction.atomic
def manufacture_update(*, manufacture: Manufacturer, data) -> Manufacturer:
    non_side_effect_fields: List[str] = [
        "name",
        "slug",
        "details",
        "image",
        "icon",
    ]

    manufacture, has_updated = model_update(instance=manufacture, fields=non_side_effect_fields, data=data)

    return manufacture


@transaction.atomic
def manufacture_delete(*, slug: str) -> None:
    manufacture = get_object(Manufacturer, slug=slug)
    manufacture.delete()
    return None
