from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from products.models import Type, Tag, Attribute, Manufacturer, Author, Category, Product


# Register your models here.
@admin.register(Type)
class Type(ImportExportModelAdmin):
    pass


@admin.register(Tag)
class Tag(ImportExportModelAdmin):
    pass


@admin.register(Attribute)
class Attribute(ImportExportModelAdmin):
    pass


@admin.register(Manufacturer)
class Manufacturer(ImportExportModelAdmin):
    pass


@admin.register(Author)
class Author(ImportExportModelAdmin):
    pass


@admin.register(Category)
class Category(ImportExportModelAdmin):
    pass


@admin.register(Product)
class Product(ImportExportModelAdmin):
    pass
