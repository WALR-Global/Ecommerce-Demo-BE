from typing import Optional

from django.db.models import QuerySet

from common.utils import get_object
from products.filters import BaseCategoryFilter
from products.models import Type, Tag, Category, Attribute, Manufacturer


def type_list(*, filters=None) -> QuerySet[Type]:
    filters = filters or {}

    qs = Type.objects.all()

    return qs

def tag_list(*, filters=None) -> QuerySet[Tag]:
    filters = filters or {}

    qs = Tag.objects.all()

    return qs

def tag_get(tag_id) -> Optional[Tag]:
    tag = get_object(Tag, id=tag_id)

    return tag


def tag_get_by_slug(slug) -> Optional[Tag]:
    tag = get_object(Tag, slug=slug)

    return tag

def category_list(*, filters=None) -> QuerySet[Category]:
    filters = filters or {}

    qs = Category.objects.all()

    return BaseCategoryFilter(filters, qs).qs


def category_get_by_slug(slug) -> Optional[Category]:
    category = get_object(Category, slug=slug)

    return category


def category_get(category_id) -> Optional[Category]:
    category = get_object(Category, id=category_id)

    return category


def attribute_list(*, filters=None) -> QuerySet[Attribute]:
    filters = filters or {}

    qs = Attribute.objects.all()

    return qs


def attribute_get_by_slug(slug) -> Optional[Attribute]:
    attribute = get_object(Attribute, slug=slug)

    return attribute


def attribute_get(attribute_id) -> Optional[Attribute]:
    attribute = get_object(Attribute, id=attribute_id)

    return attribute


def manufacturer_list(*, filters=None) -> QuerySet[Manufacturer]:
    filters = filters or {}

    qs = Manufacturer.objects.all()

    return qs
