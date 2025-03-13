from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from products.models import Type, Tag, Attribute, Manufacturer


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
