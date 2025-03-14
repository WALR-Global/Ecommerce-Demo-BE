from typing import List

from django.db import transaction

from common.services import model_update
from common.utils import get_object
from products.models import Product


@transaction.atomic
def product_create(*, name: str,
                   slug: str,
                   description: str = None,
                   product_type: str = None,
                   type: str,
                   categories: list = None,
                   tags: list = None,
                   author_id: str = None,
                   manufacturer_id: str = None,
                   ) -> Product:
    product = Product.objects.create(name=name,
                                     slug=slug,
                                     description=description,
                                     product_type=product_type,
                                     type_id=type,
                                     author_id=author_id,
                                     manufacturer_id=manufacturer_id,
                                     )

    # Add categories to the product
    if categories:
        for category in categories:
            product.categories.add(category)  # Assuming categories are instances or IDs

    # Add tags to the product
    if tags:
        for tag in tags:
            product.tags.add(tag)  # Assuming tags are instances or IDs

    return product


@transaction.atomic
def product_update(*, product: Product, data) -> Product:
    non_side_effect_fields: List[str] = [
        "name",
        "slug",
        "description",
        "image",
        "gallery",
        "unit",
    ]

    product, has_updated = model_update(instance=product, fields=non_side_effect_fields, data=data)

    # some additional task
    product.type_id = data.get("type_id")
    product.save()

    return product


@transaction.atomic
def product_delete(*, product_id: str) -> None:
    product = get_object(Product, id=product_id)
    product.delete()
    return None
